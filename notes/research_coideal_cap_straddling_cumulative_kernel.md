# A crossing between an ordinary and a marked cap gives a cumulative sum

24 November 2026. Written research proof.

The original last marked cap, an adjacent ordinary cap, and a crossing
between their two pairs give an explicit two-height boundary tensor.
Its exact zero pattern is triangular after a known permutation.
The surviving coefficients factor into a row weight and a column
weight. Removing their specified phases gives a positive weighted
cumulative-sum matrix, with an explicit first-difference inverse and
polynomial conditioning. Both original crossing signs are retained.

Both heights are input boundary coordinates before a matrix
reshaping is chosen. The singular-value bounds concern that
reshaping and the associated bilinear pairing. They do not give a
lower bound for its contraction against an arbitrary coherent exterior.

## 1. The literal last-mark boundary and its open heights

Retain the complete conventions of H, S, T and K:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 x=-q^{-1}=q^d,\quad c=1+q,\quad
 \delta=\pi/N,\quad\theta=\delta/2,\quad
 \kappa=q^{d^2/2}.
 \tag{1}
\]
All fractional powers mean these exponential branches. The physical
heads are orthonormal. The original cups and caps are
\[
 p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\qquad
 \ell_{ab}=x^a\mathbf1_{a+b=d}/N,\qquad m_{ab}=x^b/N^2.
 \tag{2}
\]
There is no degree delta on the marked row \(m\).
Let \(F_a=(Q;Q)_a\), \(F_0=1,F_d=N\), and use the continuants
\[
 D_{-1}=0,\quad D_0=1,\quad
 D_{a+1}(\lambda;\sigma)
 =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                         -q(1-Q^a)^2D_{a-1}(\lambda;\sigma).
 \tag{3}
\]
Write
\[
 \mu_j=Q^j+qQ^{-j},\quad
 \Phi_{\rho,\nu}(z)=\sum_{a=0}^dD_a(\rho;\nu)z^a/F_a,\quad
 u_\rho(\nu)_a=q^{-a}D_a(\rho;\nu)/F_a .
 \tag{4}
\]
The roots \(\mu_j\) are distinct at every level. They are the full
spectrum of each nonempty suffix coideal \(B_c=F_*-(E_*-c)K_*^{-1}\).
The path basis in H retains every physical coordinate.

First use four heads and the literal row
\[
                    r^\pm=(\ell_{12}\otimes m_{34})R_{23}^\pm
 \tag{5}
\]
on the conserved external channel \(B_c^{(4)}=c\).
Its input path heights are
\((c,\nu,\rho,\sigma,c)\), where \(\nu,\rho,\sigma\) are roots.
H's ordinary and full marked tensors give, before the crossing,
\[
 (\ell_{12}\otimes m_{34})(v_{c,\nu,\rho',\sigma,c})
   ={T_*\over A_c}\,
                   \delta_{\rho',c}\delta_{\sigma,\mu_*},\qquad
 A_\lambda={N^2q^dx^{-d}\over p_N'(\lambda)},\quad
 T_*={2\over N(1-q^{-3})},
\]
\[
 \mu_*=-q^{-1}-q^2,\qquad
 p_N(z)=2q^{N/2}T_N(z/(2\sqrt q)),\qquad
 p_N'(c)={2N\over1-q}.
 \tag{6}
\]
Here \(T_N\) is Chebyshev. These are the original last-mark
coefficients; no mark is moved across an exterior.
The crossing changes only the middle height \(\rho\) to \(\rho'\).
It preserves the neighbors \(\nu,\sigma\).

S gives its entry for the positive crossing sign in the same frame:
\[
 B^+_{\rho',\rho}(\nu,\sigma)
   ={\kappa E_d(\rho';\sigma)\over p_N'(\rho')}
       \sum_{a=0}^d{\overline{D_a(\rho;\nu)}
                                D_a(\rho';\sigma)\over|F_a|^2},
 \tag{7}
\]
where \(E_d\) is the trailing continuant.
At the observed boundary,
\(D_a(c;\mu_*)=q^aF_a\) and \(E_d(c;\mu_*)=N\).
Therefore the complete row coefficients are
\[
 r^+(v_{c,\nu,\rho,\sigma,c})
     =\delta_{\sigma,\mu_*}\,M^+_{\nu,\rho},\qquad
 M^+_{\nu,\rho}=\beta_N\,
                              \overline{\Phi_{\rho,\nu}(q^{-1})},
 \quad
 \beta_N={T_*\over A_c}{\kappa(1-q)\over2}.
 \tag{8}
\]
This is a coherent finite contraction of the actual crossing and
both caps. It is not a selected term of the crossing sum.

Both \(\nu,\rho\) in (8) are retained input boundary coordinates. For any attached
array \(Z_{\nu,\rho}\), their scalar contraction is
\(\sum_{\nu,\rho}M^+_{\nu,\rho}Z_{\nu,\rho}\).
Writing \(M\) as a matrix below is an explicit reshaping of this
two-index tensor, not a new direction of physical propagation.

## 2. Exact support at both level parities

T supplies the finite product for \(\rho=\mu_j,\nu=\mu_l\):
\[
 \Phi_{\mu_j,\mu_l}(q^{-1})
     =(-Q^l;Q)_A(-qQ^{-l};Q)_B,\quad B=d-A,\qquad
 A=\begin{cases}
       [m-j-l]_N,&N=2m,\\
       [m+j-l]_N,&N=2m+1.
     \end{cases}
 \tag{9}
\]
No endpoint or cyclic alias is removed from this identity.
Define the known permutation of row labels
\[
 t=t(l)=
 \begin{cases}[m-l]_N,&N=2m,\\
               [m+l]_N,&N=2m+1.
 \end{cases}
 \tag{10}
\]
For even \(N\), \(Q^m=-1\). The first string in (9) is the
integer-grid string \((Q^{-t};Q)_A\), which vanishes exactly when
\(A>t\). The second string is half-grid and never has a zero.
For odd \(N\), \(qQ^m=-1\); now the second string is
\((Q^{-t};Q)_B\), vanishing exactly when \(B>t\).
The first string is the nonzero half-grid string.

Let \(J=A\) in the even case and \(J=B\) in the odd case.
In both cases \(J=[t-j]_N\). Consequently
\[
 \boxed{\quad
 \Phi_{\mu_j,\mu_l}(q^{-1})=0\ \Longleftrightarrow\ j>t(l).
 \quad}
 \tag{11}
\]
If \(j\le t\), both parity cases have exactly the same product:
\[
 \Phi_{\mu_j,\mu_l}(q^{-1})
       =(Q^{-t};Q)_{t-j}(qQ^t;Q)_{d-t+j}.
 \tag{12}
\]
All factors in the first string have nonzero integer indices.
The second string has only nonzero odd half-grid indices.
Thus (11) lists every zero, including all even and composite levels.

Use the full half-grid identity
\((q;Q)_N=1-q^N=2\).
The factors missing from the second product of (12) are those
in \((qQ^{j-1};Q)_{t-j+1}\). Hence
\[
 \Phi_{\mu_j,\mu_l}(q^{-1})
  =2\,{\prod_{k=j+1}^t(1-Q^{-k})\over
                         \prod_{k=j}^t(1-q^{2k-1})}
                                      \quad(j\le t).
 \tag{13}
\]
In particular the \(j=0\) denominator retains \(1-q^{-1}\).
It is not replaced by a missing boundary factor.

## 3. The complete positive cumulative kernel

Put
\[
 U_t=\prod_{k=1}^t{1-Q^{-k}\over1-q^{2k-1}},\quad U_0=1,
 \qquad V_j={2\over U_j(1-q^{2j-1})}.
 \tag{14}
\]
Every displayed denominator is nonzero. Let
\(L_{tj}=\mathbf1_{j\le t}\), and let \(P\) be the matrix whose
row \(t(l)\), column \(j\) is \(\Phi_{\mu_j,\mu_l}(q^{-1})\).
Equations (11)--(14) prove the exact full-matrix identity
\[
 \boxed{\qquad P=\operatorname{diag}(U_t)\,
                            L\,\operatorname{diag}(V_j).\qquad}
 \tag{15}
\]
Thus the two-index boundary has rank \(N\), with its exact
triangular zeros retained. Removing the known unit phases of
\(U_t,V_j\) leaves
\(\operatorname{diag}(|U_t|)L\operatorname{diag}(|V_j|)\),
an entrywise positive kernel on that support.
For example the row phase is explicitly
\[
             U_t/|U_t|=(-1)^tq^{-t(2t+1)/2};
 \tag{16}
\]
the column phase is exactly that of \(2/[U_j(1-q^{2j-1})]\),
including its endpoint sign at \(j=0\).
For a sorted row \(\nu=\lambda_r\), H's root permutation gives
\(2t=N-\tfrac12+(-1)^{N+r}(r+\tfrac12)\), so the row phase
is also \(e^{i\pi d/4}f_r^{-1}\), with S's same
single-height chirp \(f_r=e^{i\pi r(r+1)/(4N)}\).
An inverse rephasing of an attached exterior retains the original
bilinear contraction. No phase average is performed.

There is an explicit inverse, not only a nonzero determinant:
\[
 P^{-1}=\operatorname{diag}(V_j^{-1})\,
               \nabla\,\operatorname{diag}(U_t^{-1}),\qquad
 (\nabla y)_j=y_j-y_{j-1},\quad y_{-1}=0 .
 \tag{17}
\]
The row permutation (10) is undone when returning to the original
height order. It has norm one.

For uniform costs define
\[
 R_t=|U_t|
      =\prod_{k=1}^t{\sin(k\delta)\over\sin((k-\tfrac12)\delta)}.
 \tag{18}
\]
The ratios cross one once, so \(R_t\) is unimodal; its endpoints
are \(R_0=1\), \(R_d=N\sin\theta\ge1\).
Also \(\sin v/v\) decreases on \((0,\pi)\), giving
\[
 1\le R_t\le\prod_{k=1}^t{k\over k-\tfrac12}
                 \le C\sqrt N,\qquad
 cN^{-1/2}\le|V_j|\le N.
 \tag{19}
\]
The product bound follows from
\(\sum_{k=1}^t(2k-1)^{-1}\le\tfrac12\log(t+1)+C\);
the last inequality uses \(|1-q^{2j-1}|\ge2\sin\theta\ge2/N\).
Since \(\|L\|\le N\), \(\|\nabla\|\le2\), (15)--(19) give
\[
 \boxed{\quad \|P\|\le CN^{5/2},\qquad
                \|P^{-1}\|\le C\sqrt N,\qquad
                \operatorname{cond}(P)\le CN^3.\quad}
 \tag{20}
\]
These are induced Euclidean norms on the reshaped row and column coordinates.
Every nonzero entry is between \(cN^{-1/2}\) and \(CN^{3/2}\).
Thus its logarithmic action divided by \(N\) tends uniformly to zero.
This boundary is not an additional positive-volume cell: the exact
integer and half-grid factorial actions cancel. Its support and
polynomial weights remain available to the interior volume model.

## 4. Original scalar factors, both signs, and the positive path metric

In the raw four-head two-index reshaping, (8) is, after the row
permutation, \(M^+=\beta_N\overline P\).
The exact magnitudes of H's original constants are
\[
 |A_c|=N\sin\theta,\quad |T_*|={1\over N\sin3\theta},
 \qquad |\beta_N|={1\over N^2\sin3\theta}.
 \tag{21}
\]
Here \(\sin\theta\le\sin3\theta\le3\sin\theta\) for all \(N\ge2\).
Thus \(c/N\le|\beta_N|\le C/N\), and
\[
 \|M^+\|+\|(M^+)^{-1}\|\le CN^{3/2},\qquad
                        \operatorname{cond}(M^+)\le CN^3.
 \tag{22}
\]
The scalar and its phase have not been discarded from (8).

S proves entrywise \(B^-=\overline{B^+}\) in the same height frame.
The fixed cap coefficient \(T_*/A_c\) is not conjugated when
changing the crossing sign. Consequently
\[
 M^-={T_*\over A_c}\,
          {\kappa^{-1}(1-q^{-1})\over2}\,P
       =q^6\overline{M^+}.
 \tag{23}
\]
Indeed \(T_*/\bar T_*=-q^3\), and \(\bar A_c/A_c=-q^3\).
It is not bare conjugation of the original boundary row.
The norms, inverse bounds and positive support are identical.

H's specified positive path metric is the absolute diagonal in the
complete coideal coordinates, not a physical absolute-value operator.
For this boundary its input heights are
\((c,\nu,\rho,\mu_*,c)\), and the four-head squared path weight is
\[
           \csc\theta\,\csc\alpha_\nu\,
                        \csc\alpha_\rho\,\csc3\theta,\qquad
 \alpha_\xi=\arccos(\xi/(2\sqrt q)).
 \tag{24}
\]
Both free heights are input boundary coordinates of this row tensor.
The coefficient in the orthonormal path frame is therefore
\[
 \widehat M^+_{\nu,\rho}
 =\beta_N\sqrt{\sin\theta\sin3\theta}\,
       \sqrt{\sin\alpha_\nu}\,
       \overline{\Phi_{\rho,\nu}(q^{-1})}\,
       \sqrt{\sin\alpha_\rho}.
 \tag{25}
\]
There are no omitted neighboring \(h_N\) factors: that is a
different Haar metric. The common scalar magnitude in (25) is
exactly
\[
 {1\over N^2}\sqrt{\sin\theta\over\sin3\theta}
                   \in[1/(\sqrt3N^2),\,1/N^2].
 \tag{26}
\]
The two sine diagonals have norm at most one and inverse norm at
most \(\sqrt N\). It follows that, for either sign,
\[
 \boxed{\quad
 \|\widehat M^\pm\|\le C\sqrt N,\qquad
 \|(\widehat M^\pm)^{-1}\|\le CN^{7/2},\qquad
             \operatorname{cond}(\widehat M^\pm)\le CN^4 .
 \quad}
 \tag{27}
\]
All phases and the triangular zeros are still explicit in (25).
The positive sine diagonals do not change the rephasing statement.

There is also a sparse positive gluing Gram for this specified
reshaping. In permuted row order write
\(\widehat M^+=D_aLD_b\), with the known nonzero factors
\[
 a_t=\beta_N\sqrt{\sin\theta\sin3\theta}\,
                    \sqrt{\sin\alpha_{\nu(t)}}\,\bar U_t,\qquad
 b_j=\bar V_j\sqrt{\sin\alpha_{\mu_j}}.
\]
Then \(G_{\partial}=(\widehat M^+)^{-\dagger}
(\widehat M^+)^{-1}\) has the explicit energy
\[
 \|y\|_{G_{\partial}}^2
   =\sum_{j=0}^d\left|
       {z_j-z_{j-1}\over b_j}\right|^2,
 \quad z_j=y_j/a_j,\quad z_{-1}=0,\qquad
 (\widehat M^+)^\dagger G_{\partial}\widehat M^+=I.
 \tag{27a}
\]
Thus the Gram is Hermitian tridiagonal and positive, and its
eigenvalues lie between \(c/N\) and \(CN^7\), by (27).
Its logarithmic radius is \(O(\log N)\). This is a nearest-neighbor
sum of squared linear boundary residuals, with \(N\) retained
coordinates. It uses the actual source weights, not an unknown
completed word. Here \(y\) is the output of the declared matrix
reshaping. The isometry is for that reshaping;
it does not replace the original bilinear observation by a trace.
For the original pairing \(x^{\mathsf T}\widehat M^+v\), the
matching primal metric on \(x\) is \(G_{\partial}^{-\mathsf T}\),
not \(G_{\partial}\). No terminal condition is imposed on \(y_d\).

The determinant normalization is explicit as well. In canonical
row \(t\), column \(j\) order,
\[
 \det P=2^{N-1},\qquad
 \det(P^{-\dagger}P^{-1})=4^{1-N},\qquad
 \det\widehat M^+=g_0^N,\quad
 \det G_{\partial}=|g_0|^{-2N},\quad
 g_0=\beta_N\sqrt{\sin\theta\sin3\theta}.
 \tag{27b}
\]
Indeed \(\prod_jU_jV_j=2^N/\prod_j(1-q^{2j-1})=2^{N-1}\).
The two sine diagonals in (25) have combined determinant
\(\prod_j\sin\alpha_{\mu_j}=2^{1-N}\), canceling this factor.
An original row permutation retains its determinant sign;
no scalar period is inferred from these Gram determinants.

For the original external factor \(\chi_N\), the boundary tensor
is \(\chi_NM^\pm\), or \(\chi_N\widehat M^\pm\) in (25).
Its map norm acquires \(|\chi_N|\), and its inverse, when
\(\chi_N\ne0\), acquires \(|\chi_N|^{-1}\).
Its condition number is unchanged. No polynomial bound on this
external factor is asserted.

## 5. Arbitrary fixed width and the meaning of the lower bound

For \(b=2k\ge4\), keep the prescribed original last marked cap
\(\ell_0=\ell_{12}\cdots\ell_{b-3,b-2}m_{b-1,b}\).
The crossing \(R_{b-2}\) is between the last ordinary pair and
the marked pair, rather than between two legs of one cap.
On the external channel \(\nu_0=c\), let
\(\nu=\nu_{b-3}\), \(\rho=\nu_{b-2}\).
The complete row is
\[
 \ell_0R_{b-2}^{+}(v_{\boldsymbol\nu})
 =A_c^{-(k-1)}T_*{\kappa(1-q)\over2}\,
      \overline{\Phi_{\rho,\nu}(q^{-1})}
       \left(\prod_{r=1}^{k-2}\delta_{\nu_{2r},c}\right)
                         \delta_{\nu_{b-1},\mu_*}.
 \tag{28}
\]
Every earlier free odd height and its original ordinary cap remain.
For the negative sign conjugate the face entry, retaining the same
ordinary and marked prefactors. Equivalently, the ratio of this
row to the conjugate positive row is \((-q^3)^k\), before including
\(\chi_N\). The four-head instance is (23).

Equations (28) and (15) hold for every attached state in
\(\mathcal E_c=\ker(B_c^{(b)}-c)\). They require no mark relocation
or assumption that the attached vector is a particular knot state.
The earlier ordinary caps have exact positive-metric norm
\(1/(N\sin\theta)\in[2/\pi,1]\) on the selected \(c\) sector,
by H. Their fixed-width composition introduces only known
polynomial factors. Full path normalization must include all
their retained weights, not just the two-index factors in (25).

The inverse bounds do not lower-bound every scalar contraction.
For the explicitly chosen reshaping, for example,
\[
 \|M^\pm y\|_2\ge cN^{-3/2}\|y\|_2,\qquad
 \|\widehat M^\pm y\|_2\ge cN^{-7/2}\|y\|_2.
 \tag{29}
\]
Equivalently they control the supremum of
\(|u^{\mathsf T}M^\pm y|\) over a unit vector \(u\).
They do not bound this expression below for a prescribed \(u\),
nor bound \(\sum_{\nu,\rho}M_{\nu,\rho}Z_{\nu,\rho}\) below
for an arbitrary coherent exterior array \(Z\).
No Hilbert trace replaces either of the original caps.
The ordinary, marked, framing and peripheral factors stay original.

The full physical and height maps retain all pair-Casimir first
normals. This boundary contraction legitimately forces the
Kronecker factors in (28); it is not an intermediate projection
onto a semisimple Casimir value quotient. Nor is the full
\(N^b\)-dimensional compiler silently replaced by an \(N\)-dimensional
one. The \(N\times N\) matrix is only the stated two-index reshaping.

P already proves exact ordinary-cap reassociation collapses and
retains the different full marked packet. H gives the present
height metric and the boundary crossing within a marked pair.
The addition here is the genuinely cap-straddling last-mark kernel:
its exact all-channel support, positive cumulative factorization,
explicit inverse and polynomial control with both original caps.
It has zero boundary action; no new geometric cycle, original
closed-scalar lower bound or finite-exception theorem is inferred.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| H | [Height metric and original marked boundary](research_coideal_height_pairing_and_marked_boundary.md) | 543 | bed81fcb12b20d16d41c55b476b13d8d69b1fe79d0d0620c31230ba652b1d82f |
| S | [Signed coideal volume chamber](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| T | [Exact coideal crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |
| K | [Continuant source kernel](research_coideal_continuant_source_kernel.md) | 365 | 3ea997e5258c9413fd7c771a6a1475b90b39bf731ac55c0902fd136943b26f44 |
| P | [Original pivotal cap reassociation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_pivotal_cap_reassociation_angle_packet.md) | 243 | c822bbcc34b86c600f291f7e66c210253f341319a9d92007fcc51e6633424b14 |

Only written mathematics and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
