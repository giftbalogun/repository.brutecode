# -*- coding: utf-8 -*-
"""

    Copyright (C) 2018-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

from . import JSONStore


class APIKeyStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'api_keys.json')

    def set_defaults(self):
        data = self.get_data()
        if 'keys' not in data:
            data = {'keys': {'personal': {'api_key': 'AIzaSyD2Klv5aimhLcWAKkYIQ-WvuAK-ol9S2B0', 'client_id': '1063069541721-apqiig28e72i4ot2ni0bevmv33mnigdp.apps.googleusercontent.com', 'client_secret': 'YNxXb_AchQXf5L8fP2a-tWIV'}, 'developer': {}}}
        if 'personal' not in data['keys']:
            data['keys']['personal'] = {'api_key': 'AIzaSyD2Klv5aimhLcWAKkYIQ-WvuAK-ol9S2B0', 'client_id': '1063069541721-apqiig28e72i4ot2ni0bevmv33mnigdp.apps.googleusercontent.com', 'client_secret': 'YNxXb_AchQXf5L8fP2a-tWIV'}
        if 'developer' not in data['keys']:
            data['keys']['developer'] = {}
        self.save(data)
