import unittest
import os
import shutil
from functions import create, makedir, changedir, copy, delete, file_counter, analyse


class TestCLI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create testing directory"""
        cls.test_dir = 'Test_directory'
        if not os.path.exists(cls.test_dir):
            os.mkdir(cls.test_dir)

    @classmethod
    def tearDownClass(cls):
        """Delete testing directory"""
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setUp(self):
        """Go to testing directory"""
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        """Delete all files and directory on testing directory"""
        os.chdir(self.original_dir)
        for i in os.listdir(self.test_dir):
            i_path = os.path.join(self.test_dir, i)
            if os.path.isfile(i_path):
                os.remove(i_path)
            elif os.path.isdir(i_path):
                shutil.rmtree(i_path)

    def test_create(self):
        """Testing create some file"""
        name = 'test1.txt'
        text = 'testtesttest'
        create(name, text)
        self.assertTrue(os.path.exists(name))

    def test_makedir(self):
        """Testing make some directory"""
        dir_name = 'test_folder'
        makedir(dir_name)
        self.assertTrue(os.path.exists(dir_name))
        self.assertTrue(os.path.isdir(dir_name))

    def test_changedir(self):
        """Testing change directory"""
        dir_name = 'test_folder2'
        makedir(dir_name)
        expect_path = os.path.abspath(dir_name)
        changedir(dir_name)
        self.assertEqual(os.getcwd(), expect_path)

    def test_copy(self):
        """Test copy some file or directory"""
        name = 'test1.txt'
        text = 'testtesttest'
        create(name, text)
        new_name = 'test2.txt'
        copy(name, new_name)
        self.assertTrue(os.path.exists(new_name))
        with open(new_name, 'r') as f:
            content = f.read()
        self.assertEqual(content, text)

    def test_delete_file(self):
        """Testing delete file"""
        name = 'test1.txt'
        text = 'testtesttest'
        create(name, text)
        delete(name)
        self.assertFalse(os.path.exists(name))

    def test_delete_dir(self):
        """Testing delete directory"""
        dir_name = 'test_folder'
        makedir(dir_name)
        delete(dir_name)
        self.assertFalse(os.path.exists(dir_name))

    def test_file_counter(self):
        """Testing how many files we have in directory"""
        create('test.txt', '123')
        create('test2.txt', '456')
        counter = file_counter()
        self.assertEqual(counter, 2)

    def test_analyse(self):
        """Testing how many bytes in each file in a directory"""
        name = 'test1.txt'
        text = 'testtesttest'
        create(name, text)
        size = len(text.encode('utf-8'))
        output = f'Файл {name} имеет размер {size} байт'
        result = analyse()
        self.assertIn(output, result)


if __name__ == '__main__':
    unittest.main()
