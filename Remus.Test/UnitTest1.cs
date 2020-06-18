using NUnit.Framework;

namespace Remus.Test
{
    public class Tests
    {
        [Test]
        public void Test1()
        {   
            var result = Calculator.add(5, 6);
            Assert.AreEqual(11, result);
        }

        [Test]
        public void Test2()
        {
            var result = Calculator.subtract(5, 6);
            Assert.AreEqual(-1, result);
        }
    }
}