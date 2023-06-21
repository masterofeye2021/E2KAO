import unittest
from openhab.items.item_ import Item
from openhab.SupportClasses.openhabItemType import OpenhabItemType
from openhab.SupportClasses.openhabPhysicalUnit import OpenhabPhysicalUnit
from openhab.SupportClasses.openhabOutputFormat import OpenhabOutputFormat
from openhab.SupportClasses.fontAweSomeIcon import FontAweSomeIcon
from openhab.SupportClasses.openhabGroup import OpenhabGroup
from openhab.SupportClasses.openhabTag import OpenhabTag
from openhab.SupportClasses.openhabBinding import OpenhabBinding


class ItemTestCase(unittest.TestCase):
    def setUp(self):
        group = OpenhabGroup()
        group.addGroup("Temperatur")
        group.addGroup("Window")

        self.item = Item(OpenhabItemType.SWITCH,
                         "TestItem",
                         "TestLabel",
                         FontAweSomeIcon(),
                         group,
                         OpenhabTag(),
                         OpenhabPhysicalUnit.C,
                         OpenhabOutputFormat("%.1f"),
                         OpenhabBinding()
                         )

    def test_return_type(self):
        self.assertEqual(self.item.type, "Switch",
                         '<Type> Rückgabewert ungütltig')

    def test_return_group(self):
        self.assertEqual(self.item.groups, "Temperatur, Window",
                         "<Group> Rückgabewert ungültig")


if __name__ == '__main__':
    unittest.main()
