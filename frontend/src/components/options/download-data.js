import React from "react"
import moment from "moment"
import Button from "misago/components/button"
import ajax from "misago/services/ajax"
import title from "misago/services/page-title"
import snackbar from "misago/services/snackbar"

export default class DownloadData extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      isLoading: false,
      isSubmiting: false,
      downloads: [],
    }
  }

  componentDidMount() {
    title.set({
      title: pgettext("download your data title", "Download your data"),
      parent: pgettext("forum options", "Change your options"),
    })

    this.handleLoadDownloads()
  }

  handleLoadDownloads = () => {
    ajax.get(this.props.user.api.data_downloads).then(
      (data) => {
        this.setState({
          isLoading: false,
          downloads: data,
        })
      },
      (rejection) => {
        snackbar.apiError(rejection)
      }
    )
  }

  handleRequestDataDownload = () => {
    this.setState({ isSubmiting: true })
    ajax.post(this.props.user.api.request_data_download).then(
      () => {
        this.handleLoadDownloads()
        snackbar.success(
          pgettext(
            "download your data",
            "Your request for data download has been registered."
          )
        )
        this.setState({ isSubmiting: false })
      },
      (rejection) => {
        snackbar.apiError(rejection)
        this.setState({ isSubmiting: false })
      }
    )
  }

  render() {
    return (
      <div>
        <div className="panel panel-default panel-form">
          <div className="panel-heading">
            <h3 className="panel-title">
              {pgettext("download your data title", "Download your data")}
            </h3>
          </div>
          <div className="panel-body">
            <p>
              {pgettext(
                "download your data",
                'To download your data from the site, click the "Request data download" button. Depending on amount of data to be archived and number of users wanting to download their data at same time it may take up to few days for your download to be prepared. An e-mail with notification will be sent to you when your data is ready to be downloaded.'
              )}
            </p>

            <p>
              {pgettext(
                "download your data",
                "The download will only be available for limited amount of time, after which it will be deleted from the site and marked as expired."
              )}
            </p>
          </div>
          <table className="table">
            <thead>
              <tr>
                <th>{pgettext("download your data table", "Requested on")}</th>
                <th className="col-md-4">
                  {pgettext("download your data table", "Download")}
                </th>
              </tr>
            </thead>
            <tbody>
              {this.state.downloads.map((item) => {
                return (
                  <tr key={item.id}>
                    <td style={rowStyle}>
                      {moment(item.requested_on).fromNow()}
                    </td>
                    <td>
                      <DownloadButton
                        exportFile={item.file}
                        status={item.status}
                      />
                    </td>
                  </tr>
                )
              })}
              {this.state.downloads.length == 0 ? (
                <tr>
                  <td colSpan="2">
                    {pgettext(
                      "download your data table",
                      "You have no data downloads."
                    )}
                  </td>
                </tr>
              ) : null}
            </tbody>
          </table>
          <div className="panel-footer text-right">
            <Button
              className="btn-primary"
              loading={this.state.isSubmiting}
              type="button"
              onClick={this.handleRequestDataDownload}
            >
              {pgettext("download your data btn", "Request data download")}
            </Button>
          </div>
        </div>
      </div>
    )
  }
}

const rowStyle = {
  verticalAlign: "middle",
}

const STATUS_PENDING = 0
const STATUS_PROCESSING = 1

const DownloadButton = ({ exportFile, status }) => {
  if (status === STATUS_PENDING || status === STATUS_PROCESSING) {
    return (
      <Button
        className="btn-info btn-sm btn-block"
        disabled={true}
        type="button"
      >
        {pgettext("download your data table btn", "Download is being prepared")}
      </Button>
    )
  }

  if (exportFile) {
    return (
      <a className="btn btn-success btn-sm btn-block" href={exportFile}>
        {pgettext("download your data table btn", "Download your data")}
      </a>
    )
  }

  return (
    <Button
      className="btn-default btn-sm btn-block"
      disabled={true}
      type="button"
    >
      {pgettext("download your data table btn", "Download is expired")}
    </Button>
  )
}
