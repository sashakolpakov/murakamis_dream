# The literal closing cap with a prescribed observation

Private written proof, 17 November 2026. The unmarked closing cap
agrees with the original fixed cut on the scalar open knot operator.
After a nonintertwining insertion the open operator need not be scalar.
We give a marked cap which retains any specified linear observation
of that operator. Its boundary entries and norm are explicit.
No scalarity or cancellation is used for the inserted operator.

## 1. The already evaluated open source and cap

Fix odd \(N>2\), \(q=e^{2\pi i/N}\), and the constructed braid source
of [Q]. Write its two free physical indices as \(i,j\). Its boundary
expansion, with both end-edge phases omitted from the physical array,
has the form
\[
 B_G=K_{\rm open}\sum_{i,j=0}^{N-1}
                  G(i,j)\mathcal A_a(i)\mathcal A_b(j),
 \qquad
 K_{\rm open}=N^{2c-1}\prod_{v=1}^c C_vq^{\phi_v}.       \tag{1}
\]
For the uninserted source \(G=O_\chi\). Formula (1) also defines its
replacement by an arbitrary physical array \(G\); the resulting
paired boundary tensor is unambiguous because the adapters have their
specified inverses. Any actual insertion whose boundary array has
been computed can be used for \(G\). This does not assert that two
different insertion conventions give the same array.

The actual two-tetrahedron cap of [Q, Section 5], with its neutral
phase choice, has physical row
\[
                   \ell_{\rm cap}(i,j)=N^{-2}q^i.       \tag{2}
\]
It includes its four newly interior vertices and all its edge weights.
Consequently its unmarked closing is, for arbitrary \(G\),
\[
 Z_{\rm cap}(G)=N^{-2}K_{\rm open}\sum_{i,j}q^iG(i,j).
                                                               \tag{3}
\]
The passage from (3) to a fixed-zero observation in [Q] uses the
particular identity
\(O_\chi(i,j)=q^{-i}\delta_{ij}O_\chi(0,0)\). We do not apply that
identity to a modified array \(G\).

Put
\[
 \Delta_N=NK_{\rm open}
          =\prod_{v=1}^c N^2C_vq^{\phi_v}.              \tag{4}
\]
On the injective real decoration and compatible branches of [Q],
\(|\Delta_N|=1\). These are the original retained crossing factors.

## 2. An exact cap for any covector

Specify a complex array \(\nu=(\nu_{ij})\) and its bilinear observation
\[
                  \nu(G)=\sum_{i,j}\nu_{ij}G(i,j).
                                                               \tag{5}
\]
There is no complex conjugation in (5). On the two physical end
spaces insert the diagonal operator
\[
 D_\nu=\sum_{i,j}q^{-i}\nu_{ij}
                    |i,j\rangle\langle i,j|.          \tag{6}
\]
This is an explicit boundary coupon; it need not be a Hopf morphism,
a positive operator, or a product of two one-end operators.
Multiplying the actual row (2) by (6) gives \(N^{-2}\nu\).
Thus the marked closed source \(Z_\nu\), with the same cap geometry,
charges and vertex measures, satisfies for every array \(G\)
\[
 \boxed{
 Z_\nu(G)=N^{-2}K_{\rm open}\nu(G),\qquad
 N^3Z_\nu(G)=\Delta_N\,\nu(G).
 }                                                        \tag{7}
\]
This is an identity of linear observations. It does not divide by
\(\nu(G)\), which may vanish. On the real branches in (4),
\[
                        |N^3Z_\nu(G)|=|\nu(G)|.        \tag{8}
\]
The power \(N^3\) is the normalization for this marked comparison;
it does not replace the unmarked closed normalization \(N^2\).

For the fixed-zero planar cut take
\(\nu_{ij}=\delta_{i0}\delta_{j0}\). Then
\[
                    D_\nu=E_{00}\otimes E_{00}.        \tag{9}
\]
Both free indices are fixed, exactly as in the planar definition.
For the uninserted scalar array only,
\[
                   N^3Z_{\delta_{00}}(O_\chi)
                         =N^2Z_{\rm cap}(O_\chi).      \tag{10}
\]
For a general inserted array their difference is explicitly
\[
 N^2Z_{\rm cap}(G)-N^3Z_{\delta_{00}}(G)
  =\Delta_N\left\{N^{-1}\sum_{i,j}q^iG(i,j)-G(0,0)\right\}.
                                                               \tag{11}
\]
Equation (11) is the closing discrepancy that an argument using
unmarked scalarity would otherwise lose.

An averaged observation from a different representation must be
supplied as its actual covector \(\nu\) in these end coordinates.
Equality with a fixed-zero observation on scalar operators alone
does not identify their values on nonintertwining insertions.
Formula (6) retains either specified covector without making such
an identification.

## 3. The actual face-pair insertion and its bounds

Use the boundary adapters and inverse duals of [A], unchanged. For
\(m=a,b\), write
\[
 k_m=\alpha_{m,-}-\alpha_{m,+}+h_m,\quad
 l_m=\beta_{m,-}-\beta_{m,+}+h_m,\quad
 f_m(k)=a_m^{[k-1]}b_m^{[-k]} .
\]
Their entries are
\[
 \mathcal A_m(\alpha;i)=f_m(k_m)q^{ik_m},\qquad
 \mathcal L_m(i;\beta)=\frac{q^{-il_m}}{N^2f_m(l_m)}.
                                                               \tag{12}
\]
Here residues lie in \(0,\ldots,N-1\), and \(a_m,b_m\) are the
original nonzero pole-edge roots. The face realization of (6) is
\[
 \mathcal D_\nu=(\mathcal A_a\otimes\mathcal A_b)
                   D_\nu(\mathcal L_a\otimes\mathcal L_b).
\]
In all four incoming and four outgoing face indices it is exactly
\[
 \boxed{
 (\mathcal D_\nu)_{\alpha;\beta}
 =\frac{f_a(k_a)f_b(k_b)}
        {N^4f_a(l_a)f_b(l_b)}
   \sum_{i,j}\nu_{ij}
      q^{i(k_a-l_a-1)+j(k_b-l_b)} .
 }                                                        \tag{13}
\]
It acts on the two paired invariant images and kills their specified
complementary kernels. The identities
\(\mathcal L_m\mathcal A_m=I\) show that inserting (13) into (1)
has exactly the effect of (6). Every cyclic seam and inverse
\(f_m(l_m)^{-1}\) remains; no Hermitian adjoint is substituted.
For (9), formula (13) is the product of the two literal fixed-cut
face projectors in [A].

In the standard Euclidean physical norm,
\[
                         \|D_\nu\|_2=\max_{i,j}|\nu_{ij}| .
                                                               \tag{14}
\]
Let
\(\kappa_m=\max_k|f_m(k)|/\min_k|f_m(k)|\). The exact singular
values in [A] and cancellation of the two \(N^2\) normalization
factors give
\[
 \frac{\|\nu\|_\infty}{\kappa_a\kappa_b}
 \le \|\mathcal D_\nu\|_2
 \le \kappa_a\kappa_b\|\nu\|_\infty.                  \tag{15}
\]
The norm includes the full face-pair space; the operator is zero
on the stated complementary kernel. To obtain the lower inequality,
apply the inverse coordinate map on the image to \(\mathcal D_\nu\).
On fixed compact sets of nonzero decoration differences the two
\(\kappa_m\) are bounded independently of \(N\). Thus the cap
transport itself adds no exponential norm loss to a supplied
covector. It does not bound the covector if its own coefficients
grow exponentially.

All formulas are exact at fixed odd level and preserve any further
linear combinations of inserted arrays. Regular decoration
derivatives retain the coupons, inverse rows, and scalar
\(\Delta_N\); they do not introduce an off-root level or physical
meridian family. This supplies the full marked closing observation
once the open array and its covector are specified. It does not
identify a negative-ray current with a particular insertion, transport
an analytic integration cycle, or prove a geometric lower bound.

## Complete direct sources

- [Q] [Braid cut and global sewing](research_braid_cut_and_global_nine_cell_sewing.md),
  SHA256 58503fba3cf834269943956429cc7ac6190499da5e40f57c82d8f13ef995b470.
  The whole proof was read. Its open boundary tensor, evaluated cap,
  and normalization are used.
- [A] [Paired-face boundary adapter](research_kashaev_paired_face_boundary_adapter.md),
  SHA256 c430fd2714acdc7588003e1c18c60453e1ebe123bd7c0155d20a0eef639ec8ed.
  The whole proof was read. Its exact inverse, image projector,
  fixed cut and singular values are used.

No mathematical programs or numerical experiments were used.
