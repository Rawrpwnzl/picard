# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2006 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4 import QtCore, QtGui
from picard.config import BoolOption, IntOption, TextOption
from picard.ui.options import OptionsPage, register_options_page
from picard.ui.ui_options_cover import Ui_CoverOptionsPage


class CoverOptionsPage(OptionsPage):

    NAME = "cover"
    TITLE = N_("Cover Art")
    PARENT = None
    SORT_ORDER = 35
    ACTIVE = True

    options = [
        BoolOption("setting", "save_images_to_tags", True),
        BoolOption("setting", "save_only_front_images_to_tags", False),
        BoolOption("setting", "save_images_to_files", False),
        TextOption("setting", "cover_image_filename", "cover"),
        BoolOption("setting", "save_images_overwrite", False),
        BoolOption("setting", "ca_provider_use_amazon", False),
        BoolOption("setting", "ca_provider_use_cdbaby", False),
        BoolOption("setting", "ca_provider_use_caa", False),
        BoolOption("setting", "ca_provider_use_whitelist", False),
        BoolOption("setting", "caa_approved_only", False),
        BoolOption("setting", "caa_image_type_as_filename", False),
        IntOption("setting", "caa_image_size", 2),
        TextOption("setting", "caa_image_types", "front"),
    ]

    def __init__(self, parent=None):
        super(CoverOptionsPage, self).__init__(parent)
        self.ui = Ui_CoverOptionsPage()
        self.ui.setupUi(self)
        self.ui.save_images_to_files.clicked.connect(self.update_filename)

    def load(self):
        self.ui.save_images_to_tags.setChecked(self.config.setting["save_images_to_tags"])
        self.ui.cb_embed_front_only.setChecked(self.config.setting["save_only_front_images_to_tags"])
        self.ui.save_images_to_files.setChecked(self.config.setting["save_images_to_files"])
        self.ui.cover_image_filename.setText(self.config.setting["cover_image_filename"])
        self.ui.save_images_overwrite.setChecked(self.config.setting["save_images_overwrite"])
        self.update_filename()
        self.ui.caprovider_amazon.setChecked(self.config.setting["ca_provider_use_amazon"])
        self.ui.caprovider_cdbaby.setChecked(self.config.setting["ca_provider_use_cdbaby"])
        self.ui.caprovider_caa.setChecked(self.config.setting["ca_provider_use_caa"])
        self.ui.caprovider_whitelist.setChecked(self.config.setting["ca_provider_use_whitelist"])
        self.ui.gb_caa.setEnabled(self.config.setting["ca_provider_use_caa"])

        self.ui.cb_image_size.setCurrentIndex(self.config.setting["caa_image_size"])
        self.ui.le_image_types.setText(self.config.setting["caa_image_types"])
        self.ui.cb_approved_only.setChecked(self.config.setting["caa_approved_only"])
        self.ui.cb_type_as_filename.setChecked(self.config.setting["caa_image_type_as_filename"])
        self.connect(self.ui.caprovider_caa, QtCore.SIGNAL("toggled(bool)"),
                self.ui.gb_caa.setEnabled)

    def save(self):
        self.config.setting["save_images_to_tags"] = self.ui.save_images_to_tags.isChecked()
        self.config.setting["save_only_front_images_to_tags"] = self.ui.cb_embed_front_only.isChecked()
        self.config.setting["save_images_to_files"] = self.ui.save_images_to_files.isChecked()
        self.config.setting["cover_image_filename"] = unicode(self.ui.cover_image_filename.text())
        self.config.setting["ca_provider_use_amazon"] =\
            self.ui.caprovider_amazon.isChecked()
        self.config.setting["ca_provider_use_cdbaby"] =\
            self.ui.caprovider_cdbaby.isChecked()
        self.config.setting["ca_provider_use_caa"] =\
            self.ui.caprovider_caa.isChecked()
        self.config.setting["ca_provider_use_whitelist"] =\
            self.ui.caprovider_whitelist.isChecked()
        self.config.setting["caa_image_size"] =\
            self.ui.cb_image_size.currentIndex()
        self.config.setting["caa_image_types"] = self.ui.le_image_types.text()
        self.config.setting["caa_approved_only"] =\
            self.ui.cb_approved_only.isChecked()
        self.config.setting["caa_image_type_as_filename"] = \
            self.ui.cb_type_as_filename.isChecked()

        self.config.setting["save_images_overwrite"] = self.ui.save_images_overwrite.isChecked()

    def update_filename(self):
        enabled = self.ui.save_images_to_files.isChecked()
        self.ui.cover_image_filename.setEnabled(enabled)
        self.ui.save_images_overwrite.setEnabled(enabled)


register_options_page(CoverOptionsPage)
