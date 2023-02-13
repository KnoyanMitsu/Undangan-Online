<?php

include "../config.php";





?>
<?php @include "header.php" ?>
                    <!-- Start Content-->
                    <div class="container-fluid">
                        <br>
                        <br>
                        <!-- start page title -->
                        <span><h1 class="page-title">Undangan</h1></span>
                        <!-- end page title -->
                        <!-- end row -->
                        <div class="container">
                            <div class="col-lg-13">
                                <div class="card">
                                    <div class="card-body">
                                        <?php 
                                        $qr_code = $_GET["qr_code"];
                                        $sql2 = "SELECT * from tamu where QR_Code = '".$qr_code."'";
                                        $result2 = mysqli_query($conn,$sql2);
                                        while ($row2 = mysqli_fetch_array($result2))
                                        {?>
                                            <p>Nama Tamu:</p>
                                            <h2><?php echo $row2["nama"];?></h2>
                                            <p>Email:</p>
                                            <h2><?php echo $row2["email"];?></h2>
                                            <p>Undangan:</p>
                                            <?php  
                                            $sql3 = "SELECT * from undangan where id_undangan = '".$row2["id_undangan"]."'";
                                            $result3 = mysqli_query($conn,$sql3);
                                            while ($row3 = mysqli_fetch_array($result3))
                                            {?>
                                            <h2><?php echo $row3["Judul"]?></h2>
                                            <?php }?>
                                        <?php } ?>  
                                        </div>  
                                        </div>
                                    </div>
                                    </div> <!-- end card-body-->
                                </div> <!-- end card-->
                            </div> <!-- end col-->

                        <!-- end row -->
                    </div>
                    <!-- container -->
                       
                </div>
                <!-- content -->
                <?php @include "footer.php" ?>