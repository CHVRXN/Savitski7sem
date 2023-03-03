using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SF2022User5Lib
{
    public class Class1
    {
      public static double MinAVG(string[] marks)
      {
            int sum = 0;
            double result;
            for (int i = 0; i < marks.Length; i++)
                sum += Convert.ToInt32(marks[1]);
            if (marks.Length != 0)
                result = sum / marks.Length;
            else
                result = 0;
            return result;
      }
        
    }
}
