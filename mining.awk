#usage is awk -f <script> <filenames>
/upload/{ if ($10 ==0)
	   {
	     name=$16;
             i=index(name,":");
             if(i>0)
               { name=substr(name,1,i-1); }
	     sizes[name]+=$7;
	     numfiles[name]++;
	   }
        }

END{
       for ( u in sizes )
         {
            size=sizes[u];
            unit="Byte";
           if( sizes[u] > 1048576)
             {  size= sizes[u]/(1048576);
                unit="MB";
             }
           else if(sizes[u]>1024)
             {
	        size=sizes[u]/1024;
		unit="KB";
	     }
          printf("username:%-20s uploaded %-6d %-5s size of %-5d files \n",u,size,unit,numfiles[u]);
             
         } 

   }


