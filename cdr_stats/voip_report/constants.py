#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.utils.translation import ugettext as _
from common.utils import Choice


class BILLED_STATUS_LIST(Choice):
    all = 'all', _('ALL')
    yes = 'yes', _('YES')
    no = 'no', _('NO')


class CONFIRMATION_TYPE(Choice):
    YES = 'YES', _('Yes')
    NO = 'NO', _('No')
