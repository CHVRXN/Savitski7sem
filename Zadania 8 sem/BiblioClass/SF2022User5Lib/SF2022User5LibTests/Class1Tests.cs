using Microsoft.VisualStudio.TestTools.UnitTesting;
using SF2022User5Lib;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SF2022User5Lib.Tests
{
    [TestClass()]
    public class Class1Tests
    {
        [TestMethod()]
        public void MinAVGTest()
        {
            double expected = 5;
            string[] marks = new string[] { "5", "5", "5" };
            double actual = SF2022User5Lib.Class1.MinAVG(marks);
            Assert.AreEqual(expected, actual);
        }
        [TestMethod()]
        public void ReturnZero()
        {
            double expected = 0;
            string[] marks = new string[] {};
            double actual = SF2022User5Lib.Class1.MinAVG(marks);
            Assert.AreEqual(expected, actual);
        }
    }
}