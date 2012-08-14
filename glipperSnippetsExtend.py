#!/usr/bin/python
# coding:utf-8


import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.editor  = QtGui.QLineEdit()
        self.editor.setObjectName( "editor" )
        
        self.button  = QtGui.QPushButton( self.trUtf8( "OK" ), self )
        self.button.setObjectName( "button" )
        
        grid = QtGui.QGridLayout()
        grid.addWidget( editor, 1, 0 )
        grid.addWidget( button )
        self.setLayout( grid )

        QtCore.QMetaObject.connectSlotsByName( self )
    
    @QtCore.pyqtSlot( str, name="on_button_value" )
    def get_str_value( self, s):
        print(s)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())

import os
import sys

PLUGIN_DIRECTRY="/usr/share/glipper/plugins/"
#PLUGIN_DIRECTRY="/home/kondo/codes/glipper/glipper-2.3/glipper/plugins/"
#PLUGIN_DIRECTRY= "/home/kondo/codes/glipper/glipperSnippetsExtend/"
UI_DIRECTRY    ="/usr/share/glipper/plugins/"

CATEGORY_NAME  = sys.argv[1]

# ファイルを読み込み書き込む
def readSourceFile():
    src_filePath  = "snippets.py"
    dist_filePath = PLUGIN_DIRECTRY + CATEGORY_NAME + ".py"
    if not os.path.exists(src_filePath):
        #print "file "+src_filePath+ " is not found!!!!"
        return 1
    
    fp_src  = open( src_filePath,  'r' )
    fp_dist = open( dist_filePath, 'w' )

    for row in fp_src:
        fp_dist.write( str( replaceStringorNot( row ) ) )
    
    fp_src.close()
    fp_dist.close()

# 条件に一致した文字列を引数の文字列に変換
def replaceStringorNot( input_str ):
    counter = 0
    replaceStr = ["\'snippets\'",\
                  "snippets.ui",\
		  #"self.snippets_column = gtk.TreeViewColumn (_(\"snippets\"), self.snippets_text, text = 0)",\
                  "\"Snippets\""]

    for replace in replaceStr:
        import re
        if re.search( replace, input_str ):
            if counter == 2:
                retval = input_str.replace( "Snippets", CATEGORY_NAME )
            else:
                retval = input_str.replace( "snippets", CATEGORY_NAME )
            return retval
        counter = counter + 1
    return input_str

#if __name__ == '__main__':
#    import shutil
#    shutil.copyfile( "snippets.ui", UI_DIRECTRY + CATEGORY_NAME + ".ui" )
#    readSourceFile()
