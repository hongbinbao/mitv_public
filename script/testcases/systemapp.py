#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from uiautomatorplug.android import device as d

class SystemAppTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        d.wakeup()
        for i in xrange(3): d.press('back')
        d.press('home')
        d.press('home')
        for i in xrange(8): d.press('left')

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        for i in xrange(8): d.press('back')
        d.press('home')
        d.press('home') 

    def testLaunchAndExitAppStore(self):
        """
        launch  app store and exit
       """
        assert d(text="应用商店").exists, 'App Store icon not found!'
        d(text="应用商店").sibling(className='android.view.View').click.wait()
        assert d(resourceId='com.xiaomi.mitv.appstore:id/tv_tab_recommend', text='推荐').wait.exists(timeout=10000), 'launch App Store failed!'
        d.press('back')
        assert d(text="应用商店").wait.exists(timeout=10000), 'exit from App Store failed!'
        #d(resourceId="com.xiaomi.mitv.appstore:id/title_chinese_textview",text='应 用商店').wait.exists()

    def testLaunchAndExitCloudGallery(self):
        """
        launch  app store and exit
       """
        for i in xrange(8):
            d.press('right')
        assert d(text="云相册").exists, 'Cloud Gallery icon not found!'
        d(text="云相册").click.wait()
        #gallery_check_png =  os.path.join(PIC_DIR, 'cloudgallery_sub_1.png')
        d.expect('cloudgallery_sub_1.png', timeout=20000)
        d.press('back')
        assert d(text="云相册").wait.exists(timeout=10000), 'exit from cloud gallery failed!'
        #d(resourceId="com.xiaomi.mitv.appstore:id/title_chinese_textview",text='应 用商店').wait.exists()

    def  testLaunchAndExitFM(self):
        for i in xrange(8):
            d.press('right')
        assert d(text="网络电台").exists, 'FM app icon not found!'
        d(text="网络电台").click.wait()
        assert d(resourceId='com.xiaomi.mimusic:id/play_btn').child(className='android.widget.ImageView').wait.exists(timeout=10000), 'Open FM failed!'
        d.sleep(10)
        d.press('back')
        d.sleep(2)
        d.press('back')
        assert d(text="网络电台").wait.exists(timeout=10000), 'exit from FM failed!'

    def  testLaunchAndExitVideo(self):
        assert d(text="在线影视").exists, 'Online Video icon not found!'
        d(text="在线影视").sibling(className='android.view.View').click.wait()
        #menu_hot_highlight_focus_png =  os.path.join(PIC_DIR, 'menu_hot_highlight_focus.png')
        #menu_hot_highlight_nofocus_png  =  os.path.join(PIC_DIR, 'menu_hot_highlight_nofocus.png')
        if  d.find('menu_hot_highlight_focus.png', timeout=50) :
            pass
        elif  d.find('menu_hot_highlight_nofocus.png', timeout=50):
            pass
        else:
            assert False, 'open online video failed!' 
        d.press('back')
        assert d(text="在线影视").wait.exists(timeout=10000), 'exit from online video failed!'

    def testLaunchAndExitGameCenter(self):
        """
        launch  app store and exit
       """
        assert d(text="游戏中心").exists, 'Game Center icon not found!'
        d(text="游戏中心").sibling(className='android.view.View').click.wait() 
        #assert d(className='android.widget.FrameLayout').child(text="热门精选").wait.exists(timeout=20000), 'Launch Game Center failed!'
        assert d(resourceId='android:id/content').child(text="推荐").wait.exists(timeout=20000), 'Launch Game Center failed!'
        d.press('home') 
        assert d(text="游戏中心").wait.exists(timeout=10000), 'exit from Game Center failed!'

    def testLaunchAndExitSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
        assert d(text="小米电视设置").exists, 'MiTv Setting icon not found!'
        d(text="小米电视设置").click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiTv setting failed!'
        assert d(text="图像与声音").wait.exists(timeout=5000), 'launch MiTv setting failed!'
        assert d(text="关于").wait.exists(timeout=5000), 'open MiTv setting failed!'
        d.press('back') 
        assert d(text="小米电视设置").wait.exists(timeout=10000), 'exit from MiTv Setting failed!'

    def testLaunchAndExitMiracast(self):
        for i in xrange(4):
            d.press('right')
        assert d(text="无线显示").exists, 'Miracast icon not found!'
        d(text="无线显示").click.wait()
        d.press('back')
        assert d(text="无线显示").wait.exists(timeout=10000), 'exit from Miracast failed!'

    def testLaunchAndExitMediaExplorer(self):
        for i in xrange(6):
            d.press('right')
        assert d(text="高清播放器").exists, 'Media Explorer icon not found!'
        d(text="高清播放器").click.wait()
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/dev', text='设备').wait.exists(timeout=5000), 'launch Media Explorer failed!'
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/video', text="视频").wait.exists(timeout=5000), 'launch Media Explorer failed!'
        d.press('back')
        d.sleep(3)
        d.press('back')
        assert d(text="高清播放器").wait.exists(timeout=10000), 'exit from Media Explorer failed!'

    def testWifiOpenAndClose(self):
        d.start_activity('--activity-clear-task', component='com.android.settings/.Settings')
        d(text="无线和网络").wait.exists(timeout=2000)
        #d(className="android.widget.ListView", resourceId="android:id/list").child(text='WLAN').click.wait()
        #d(text="WLAN").click.wait()
        d.press('enter')
        d(resourceId='android:id/action_bar').child(text='WLAN').wait.exists(timeout=3000)
        if d(className='android.widget.Switch', text='打开').exists:
            d.press('right')
            d.sleep(2)
            d.press('up')
            d.sleep(2)
            for i in xrange(10):
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='关闭').wait.exists(timeout=3000), 'wifi close failed!'
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi open failed!' 
                assert d(resourceId='android:id/list').child(text='已连接').wait.exists(timeout=20000), 'wifi connect failed!' 
        elif d(className='android.widget.Switch', text='关闭').exists:
            d.press('right')
            d.sleep(2)
            d.press('up')
            d.sleep(2)
            for i in xrange(10):           
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi close failed!'
                assert d(resourceId='android:id/list').child(text='已连接').wait.exists(timeout=20000), 'wifi connect failed!' 
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi open failed!' 
