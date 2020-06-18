using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Threading.Tasks;

namespace Remus
{
    public class Service : IService
    {
        static int value;
        
        public int getValue()
        {
            return value;
        }

        public void setValue(int newValue)
        {
            value = newValue;
        }
    }
}
