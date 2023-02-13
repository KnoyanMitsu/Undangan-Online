<?php
    include "config.php";
    $tamu= $_GET["tamu"];
    $sql="SELECT * FROM tamu Where id_tamu='".$tamu."'";
    $result = mysqli_query($conn,$sql);
    while ($row = mysqli_fetch_array($result))
    {
        
        ?>
<?php @include "header.php"?>
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
                                        <div>
                                            <h1>Anda di undangan</h1> 

                                            <h2><?php echo $row["nama"]?></h2>
                         <?php


                                        $sql2="SELECT * FROM undangan Where id_undangan='".$row["id_undangan"]."'";
                                            $result2 = mysqli_query($conn,$sql2);
                                        while ($row2 = mysqli_fetch_array($result2))
                                        {

                                        ?>
                                        <div>
                                        <a class="btn btn-primary" href="Redirect.php?id_tema=<?php echo $row2["id_kategori"] ?>&id_undangan=<?php echo $row2["id_undangan"] ?>"> klik sini untuk membuka undangan </a>
                                        </div>


                                        <?php
                                        }
                                        ?>
                                            <img src="./upload/qrcode-img/<?php echo $row["QR_Code"]?>.png" alt="">
                                            </div>
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
                <?php @include "footer.php"?>
            <?php
    }
    
?>