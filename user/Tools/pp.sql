SELECT users.name, undangan.id_undangan AS JumlahUndangan FROM undangan, users where undangan.id_user = users.id_user GROUP BY users.name;
SELECT users.name, undangan.Judul FROM undangan, users  WHERE users.id_user = undangan.id_user  ORDER BY `undangan`.`Judul` ASC;

SELECT Judul, kategori.nama FROM undangan , kategori  WHERE undangan.id_kategori = kategori.id_kategori;