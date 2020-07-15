import os
import signal
import subprocess
import time

import allure
import pytest
import yaml

from appium_xueqiu.page.app import App

projectpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/resource/'
videpath = projectpath + 'videos/'
imagepath = projectpath + 'images/'


class TestSearch():
    def setup_class(self):
        self.app = App()
        self.search = self.app.start().main().goto_market().goto_search()

    @pytest.mark.parametrize("name", yaml.safe_load(open("./test_search.yaml", encoding="utf-8")))
    def test_search(self, name):
        videfile = videpath + 'video_' + str(time.time()) + '.mp4'
        imagefile = imagepath + "searchresult.png"
        p = subprocess.Popen(f"scrcpy -r {videfile}", shell=True)
        try:
            self.search.search(name)
            if self.search.is_choose(name):
                self.search.reset(name)
            self.search.add(name)
            assert self.search.is_choose(name)

        finally:
            self.search.get_screenshot(imagefile)
            os.kill(p.pid, signal.SIGTERM)
            time.sleep(2)
            allure.attach.file(imagefile, name='截图', attachment_type=allure.attachment_type.PNG)
            allure.attach.file(videfile, name='视频', attachment_type=allure.attachment_type.MP4)

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()
