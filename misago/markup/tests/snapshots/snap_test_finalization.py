# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_finalization_sets_translation_strings_in_empty_quotes_headings 1"
] = '<div class="quote-heading" data-noquote="1">Quoted message:</div>'

snapshots[
    "test_finalization_sets_translation_strings_in_spoilers_buttons 1"
] = '<button class="spoiler-reveal" type="button">Reveal spoiler</button>'
