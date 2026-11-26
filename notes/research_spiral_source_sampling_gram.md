# A uniformly controlled full sampling frame near the geometric boundary

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Angle-weighted damping moves the physical Fourier sampling points onto
a logarithmic spiral. The complete sampling frame remains uniformly
invertible when the logarithmic damping is at most a fixed constant
divided by the quantum level. This gives an explicit positive Gram
and an exact bilinear sewing for every boundary channel. It does not
replace the original sewing by the matched complementary point pairs.

The construction preserves the original finite source and all Casimir
first normals. The local geometric source estimates apply at its
strict-angle nodes. No noncancellation theorem for the whole assembled
source follows from the conditioning of this frame.

## 1. The actual full boundary frame

Fix \(N\ge2\), \(d=N-1\), and use the centered basis
\(f_0,\ldots,f_d\) of the complete Newton algebra. Its positive
Hermitian norm makes this basis orthonormal, while its original
bilinear Frobenius form satisfies
\[
 \phi(f_af_b)=\delta_{ab},\qquad Jf_a=f_{d-a},\qquad
 R^+=\sqrt N f_0,\quad R^-=\sqrt N f_d .
 \tag{1}
\]
No quotient by the Casimir nilpotents is taken. Write
\[
 \mathcal F_N(t)=\sum_{a=0}^d f_at^a,\qquad
 \xi_j=\frac{j+1/2}{N},\qquad
 t_j(h)=-e^{-(h+2\pi i)\xi_j},\qquad 0\le j\le d,
 \tag{2}
\]
where \(h\ge0\). The common radial parameter is \(r=e^{-h}\),
so \(|t_j(h)|=r^{\xi_j}\), exactly the angle-weighted rule.
Define the full packets
\[
 E_j(h)=\frac{\mathcal F_N(t_j(h))}{\sqrt N},\qquad
 B(h)_{aj}=\frac{t_j(h)^a}{\sqrt N}.
 \tag{3}
\]
Thus the columns of \(B\) synthesize these packets in the original
centered coordinates.

At \(h=0\), put \(V=B(0)\). Finite geometric sums give
\[
                         V^*V=I,\qquad V^{\mathsf T}V=P,
 \quad P_{ij}=\mathbf1_{i+j=d}.
 \tag{4}
\]
For the second identity, \(t_i(0)t_j(0)\) is an \(N\)-th root
of one, equal to one exactly when \(i+j=d\). There is no wrap
ambiguity because \(0\le i+j\le2d\).

The physical Newton initializer is also exact. With
\[
 q=e^{\pi i/N},\quad \kappa=q^{d^2/2},\qquad
 \gamma_j=\exp\!\left[-\frac{\pi id}{N}(j-d/2)\right],
\]
the centered Fourier sum gives
\[
                            E_j(0)=\gamma_j e_j.
 \tag{5}
\]
Indeed its Newton row \(s\) is \(\gamma_s\) times
\(N^{-1}\sum_a e^{2\pi ia(s-j)/N}\).
Thus this is a deformation of the complete original Newton frame,
with its recorded unit phases, rather than sampling only distinct
Casimir values.

## 2. A uniform full-matrix bound

Let \(A=\operatorname{diag}(0,1,\ldots,d)\) act on the row
index, and let \(X=\operatorname{diag}(\xi_0,\ldots,\xi_d)\)
act on the column index. Entrywise Taylor expansion is the exact
operator-norm convergent series
\[
                   B(h)=\sum_{k=0}^{\infty}
                         \frac{(-h)^k}{k!}A^kVX^k.
 \tag{6}
\]
Because \(V\) is unitary and \(\|X\|<1\),
\[
              \|B(h)-V\|\le e^{hd\|X\|}-1\le e^{hd}-1.
 \tag{7}
\]
This bounds the full matrix, including every off-diagonal Gram
entry, rather than only its values on complementary node pairs.

**Theorem.** Fix \(0<c<\log2\), and suppose
\(0\le h_N\le c/N\). Set
\[
                         m=2-e^c>0,\qquad M=e^c.
 \tag{8}
\]
Every singular value of \(B(h_N)\) lies in \([m,M]\).
In particular the packets in (3) form a full basis and
\[
 \begin{gathered}
 H=B^*B>0,\qquad m^2I\le H\le M^2I,\\
 M^{-2}I\le H^{-1}\le m^{-2}I.
 \end{gathered}
 \tag{9}
\]
The constants do not depend on \(N\). If \(Nh_N\to0\),
then \(H\to I\) and \(B^{\mathsf T}B\to P\) in operator norm.

**Proof.** For every vector \(v\), (7) and \(V^*V=I\) give
\[
 (1-\delta_N)\|v\|\le\|Bv\|\le(1+\delta_N)\|v\|,
 \qquad \delta_N=e^{h_Nd}-1\le e^c-1<1.
\]
This proves the singular-value and Gram bounds. If \(Nh_N\to0\),
then \(\delta_N\to0\). Both Gram differences have norm at most
\(\delta_N(2+\delta_N)\), proving their asserted limits.
\(\square\)

The exact points in (2) are distinct even for larger \(h\), since
they form a geometric progression with distinct phases. The theorem
does not assert a uniform condition bound when \(h\) is fixed as
\(N\) grows.

## 3. Matched complementary points are not an orthogonal frame

There is an exact diagnostic for a tempting incomplete repair.
Set
\[
                 R_h=\operatorname{diag}(e^{ha})_{a=0}^d,
 \qquad z_h=e^{-(h+2\pi i)/N}.
\]
For \(k=i+j-d\), a finite geometric sum gives
\[
 (B^{\mathsf T}R_hB)_{ij}=
 \begin{cases}
 1,&k=0,\\[2pt]
 \displaystyle\frac{1-e^{-hk}}{N(1-z_h^k)},&k\ne0.
 \end{cases}
 \tag{10}
\]
Indeed \(e^ht_i(h)t_j(h)=z_h^k\).
For every \(h>0\), all displayed \(k\ne0\) entries are nonzero.
The diagonal correction restores the complementary pair values,
but does not remove the off-diagonal entries. The full Gram and
inverse in (9), not only the matched pairs, are controlled by (7).

At a single fixed angular center \(\xi\), the simpler coefficient
rescaling does have a precise typing. If
\(D_\xi=\operatorname{diag}(r^{\xi a})\), then the original
diagonal bilinear sewing obeys
\[
                D_\xi^{\mathsf T}R_hD_{1-\xi}=I,
                    \qquad r=e^{-h}.
 \tag{11}
\]
For an anti-diagonal sewing the correction instead has entries
\(\mathbf1_{a+b=d}r^{-\xi a-(1-\xi)b}\).
Neither formula identifies the matrices obtained when \(\xi\)
varies with the sampling node; (10) is their full-matrix audit.

## 4. Exact source-preserving assembly

Two Grams have different jobs. For packets with new coordinate
columns \(u,v\), the unchanged positive norm and the original
bilinear form are respectively
\[
 \|Bu\|^2=u^*Hu,\qquad
 \phi((Bu)(Bv))=u^{\mathsf T}Sv,\qquad
                         S=B^{\mathsf T}B.
 \tag{12}
\]
Here \(Bu\) denotes the centered coordinate column of the packet.
The complex symmetric \(S\) is invertible, with
\(\|S\|\le M^2\) and \(\|S^{-1}\|\le m^{-2}\).
It must not be replaced by the positive Hermitian \(H\).

Let \(M_f\) denote the original bilinear multiplication written in
the centered coordinates. In an operator compiler, transport every
original tensor literally:
\[
 \begin{split}
 M_E&=B^{-1}M_f(B\otimes B),\qquad J_E=B^{-1}PB,\\
 R_E^\pm&=B^{-1}(\sqrt N\,\delta_{0\ {m or}\ d}),
                 \qquad \ell_E=\ell_f B .
 \end{split}
 \tag{13}
\]
The row \(\ell_f\) is whichever original closing is prescribed;
it includes its actual marks and normalization. Inserting (13)
into a fixed expression cancels each adjacent \(B B^{-1}\),
so its complete scalar source is exactly unchanged.

Equivalently use covariant vertex tensors
\[
 T^E_{ijk}=\phi(E_iE_jE_k)
       =N^{-3/2}\mathcal C_N(t_i(h),t_j(h),t_k(h)).
 \tag{14}
\]
Sew their lowered boundary indices with \(S^{-1}\).
A physical state \(R\) at a univalent vertex has lowered entries
\(\phi(RE_i)\); a closing functional has its entries
\(\ell(E_i)\). A turn may be retained as the covariant tensor
\(\phi(E_iJE_j)\), or as the literal operator in (13).
These conventions give the same unchanged contraction: the dual
basis is \(E^i=\sum_j(S^{-1})_{ji}E_j\), since
\(\phi(E_kE^i)=\delta_k^i\).

With the positive metric \(H\), \(B\) is an isometry onto the
old Newton norm. Consequently all properly transported vector,
Hilbert--Schmidt and source-dual norms are exactly the original
ones. A previously chosen compiler tree therefore keeps its
original budgets if these transported metrics are used.
Using flat new coordinates instead costs only the constants in
(8)--(9) for each fixed tensor; it does not justify deleting the
complex bilinear sewing or a closing phase.

All \(N\) directions are retained. In particular no information
in the full repeated-root Casimir algebra is lost by interpreting
the basis as an invertible packet sampling frame.

## 5. The local geometric estimates apply in this thin layer

Take a sequence \(0\le h_N\le c/N\). For a node triple with
\((\xi_i,\xi_j,\xi_k)\) in a fixed strict positive-prism compact,
the nodes in (2) have exactly the weighted path parameters of the
geometric source theorem, with \(r_N=e^{-h_N}\). That theorem gives
\[
 T^E_{ijk}=N^{-3/2}\kappa e^{i\pi/4-\pi i/(2N)}
  [(1-t_it_j)(1-t_it_k)(1-t_jt_k)]^{-1/2}
    e^{iN\Psi(t_i,t_j,t_k)}(1+O(N^{-1})).
 \tag{15}
\]
The action and branches are the initialized ones in the
weighted-path theorem, also when two node labels coincide.
The estimate is uniform because \(r_N\) stays in a fixed positive
compact interval including one.

The same theorem gives the covariant positive-crossing block,
on a fixed strict tetrahedron-angle compact:
\[
 \phi(R^+E_iE_j)=N^{-1}\mathcal K_N^+(t_i,t_j)
 =N^{-1/2}\kappa e^{i\pi/4-\pi i/(4N)}
       (1-t_it_j)^{-1/2}e^{iN\Psi_0(t_i,t_j)}
                                         (1+O(N^{-1})).
 \tag{16}
\]
Raising an index to form the multiplication operator still uses
the complete \(S^{-1}\). The inverse crossing retains its actual
reciprocal/conjugate chart, not a phase change of (16).

These are local asymptotics of the actual covariant tensors in a
uniformly controlled full frame. They do not estimate the tensor
mass outside the stated strict angle regions, choose compatible
attachment polarizations, or prevent cancellation after the full
bilinear sewing and marked closing. Nor does sampling on a spiral
replace the original closed Taylor circles by a spiral contour.
The exact basis identities above require no such deformation.

## Complete proof sources

Both entire matching proof texts were read:

| Source | SHA-256 |
|---|---|
| [Centered original source compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Angle-weighted geometric source path](research_angle_weighted_geometric_source_path.md) | 5f95115b02515db314183b7e581ddc11c6852191d7764547545103986f628f2d |

The matrix estimate and exact Gram/dual transport are proved above.
No novelty is claimed for perturbing a unitary matrix or changing
tensor coordinates. The application keeps the full damped physical
sampling frame, its original bilinear source and its local geometric
packets in the same controlled thin layer.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
