using System;
using calcclasslib101;





namespace TestProject1
{
    [TestClass]
    public class UnitTest1
    {
        calc mycalc = new calc();
        int[] nums = new int[] { 2, 3, 4, 5, 6 };
        [TestMethod]
        public void Testavarage()
        {



            // act
            var result = mycalc.Avarage(nums);
            // assert
            Assert.IsTrue(result == 4);
        }

         [TestMethod]
        public void Testlargest()
        {



            // act
            var result = mycalc.largest(nums);
            Assert.IsTrue(result == 6);
        }
        [TestMethod]
        public void Testsmallest()
        {



            // act
            var result = mycalc.smallest(nums);
            // assert
            Assert.IsTrue(result == 2);
        }
    }
}