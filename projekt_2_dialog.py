# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt2
                                 A QGIS plugin
 3
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-06-05
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Aleksandra Jaczewska Alicja Kowaluk
        email                : 01179140@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets, QtCore
from qgis.utils import iface
from qgis.core import QgsWkbTypes

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'projekt_2_dialog_base.ui'))

class Projekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Projekt2Dialog, self).__init__(parent)
        self.setupUi(self)
        self.button_box.accepted.connect(self.wtyczka)
        self.wczytaj_punkty()

    def wczytaj_punkty(self):
        self.punkty_lista.clear()
        warstwa = iface.activeLayer()
        if not warstwa:
            iface.messageBar().pushMessage("Error", "Nie ma aktywnej warstwy", level=2)
            return
        if warstwa.geometryType() != QgsWkbTypes.PointGeometry:
            iface.messageBar().pushMessage("Error", "Aktywna warstwa nie jest warstwą punktową", level=2)
            return
        for feature in warstwa.getFeatures():
            item = QtWidgets.QListWidgetItem(f"ID punktu: {feature.id()}")
            item.setData(QtCore.Qt.UserRole, feature)
            self.punkty_lista.addItem(item) 
    def wtyczka(self):
        selected_items = self.punkty_lista.selectedItems()
        punkty = [item.data(QtCore.Qt.UserRole) for item in selected_items]

        if len(punkty) == 2:
            h = round((abs(punkty[0].attribute('wysokosc') - punkty[1].attribute('wysokosc'))), 2)

            iface.messageBar().pushMessage("Wynik", f"Różnica wysokości między punktami o numerach ID {punkty[0].id()} i {punkty[1].id()} wynosi: {h} [m]", level=0)
        elif len(punkty) >= 3:
            xy = [(p.geometry().asPoint().x(), p.geometry().asPoint().y()) for p in punkty]

            n = len(xy)
            pole = 0.0
            for i in range(n):
                x1, y1 = xy[i]
                x2, y2 = xy[(i + 1) % n]
                pole += x1 * y2 - y1 * x2
            pole = round ((abs(pole) / 2.0), 2)

            id_punkty = ", ".join(str(p.id()) for p in punkty)

            iface.messageBar().pushMessage("Wynik", f"Pole powierzchni figury o wierzchołkach w punktach o numerach {id_punkty} wynosi: {pole} [m2]", level=0)
        else:
            iface.messageBar().pushMessage("Error", "Zbyt mała liczba zaznaczonych punktów", level=2)
    
