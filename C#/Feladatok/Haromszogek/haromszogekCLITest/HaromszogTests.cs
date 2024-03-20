using Microsoft.VisualStudio.TestTools.UnitTesting;
using haromszogekCLI;
using System;

namespace haromszogekCLI.Test
{
    [TestClass()]
    public class HaromszogTests
    {
        [TestMethod()]
        public void DerekszoguTest()
        {
            // Arrange
            string line = "3 4 5"; // Sample input string
            Haromszog haromszog = new Haromszog(line);

            // Act
            bool result = haromszog.derekszogu(haromszog.a, haromszog.b, haromszog.c);

            // Assert
            Assert.IsTrue(result);
        }
    }
}