#! /bin/bash
#execution awk -f <script> inputfile

BEGIN{pos=":";}

/upload/{ if ($10 ==0)
	   {
	     fullname=$16;
             i=index(fullname,pos);
             if(i>0)
               { name=substr(fullname,1,i-1); }
             else
               { name=fullname; }
	     sizes[name]+=$7;
	     numfiles[name]++;
	   }
        }

END{
       for ( u in sizes )
         {
           if( sizes[u] > 1048576)
             {  size= sizes[u]/2048;
            printf( "username:%-20s uploaded %-6d MB of file \n",u,size);
             }
           else if (sizes[u]>1024)
             {
		
               size=sizes[u]/1024;
	    printf( "username:%-20s uploaded %-6d KB of file \n",u,size);
	     }
           else
             {
            printf("username:%-20s uploaded %-6d Byte of file \n",u,sizes[u]);
             }
         } 
        printf("\n\n");

       for (n in numfiles)
         { 
	   printf("username:%-20s uploaded %-6d number of files \n",n,numfiles[n]);
	 }
   }

