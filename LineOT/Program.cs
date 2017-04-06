using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Thrift.Transport;
using Thrift.Protocol;
using Thrift.Collections;
using Thrift.Server;
using System.Threading.Tasks;

namespace LineOT
{
    class Program
    {
        static void Main(string[] args)
        {
            var transport = new TSocket("localhost", 9090);
        }
    }
}
