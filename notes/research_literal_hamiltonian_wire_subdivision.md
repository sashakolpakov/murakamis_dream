# A literal two-cell subdivision of the marked Hamiltonian wire

Private written proof, 17 November 2026. A two-tetrahedron ball with
its actual link edge has the paired-boundary tensor \(Z^{-1}/N\).
Its composition with the normalized joining tensor \(NZ\) is the
identity. We prove this in both endpoint orders, retaining the
original fixed cut \(E_{00}\), the face permutation maps, and all
edge and vertex measures. No free-vertex deletion or global
geometric-period assertion is used.

## 1. The ball, its orders, and its two charge assignments

Let \(N>2\) be odd, \(d=N-1\), \(q\) primitive, and
\(\epsilon=1/2\) in \(\mathbb Z/N\mathbb Z\). All indices and
charges are cyclic. Choose four distinct vertex decorations and
compatible nonzero roots \(s_{ij}^N=z_i-z_j\), with
\(s_{ji}=-s_{ij}\). Normalization roots are the shared ones of [B].

Start with order
\[
             (0,1,2,3)=(\mathsf P,L,\mathsf S,R).
                                                               \tag{1}
\]
Glue a positive and a negative tetrahedron, preserving vertex
labels, on faces \(0\) and \(2\). These two faces form a disk.
The result is a ball; its sole interior edge is \(13=LR\).
Declare that edge to be the link. Its boundary is the union of
two two-triangle disks, with material vertices \(L\) and \(R\).
At the \(L\) disk the triangles are glued along
\(\mathsf P-L-\mathsf S\); at the \(R\) disk along
\(\mathsf P-R-\mathsf S\). Their common boundary consists of
two distinct \(\mathsf P\mathsf S\) edges. Each material vertex
is interior to its port disk, although all four vertices are on
the boundary of the ball.

Write a tetrahedral charge triple as \((a,b,c)\) on opposite
pairs \(01|23,02|13,03|12\), with \(a+b+c=\epsilon\).
Use the same triple on the two cells, choosing either
\[
\begin{array}{c|c|c|c}
 &\text{triple in (1)}&
 (h_L,h_R)&\text{triple in }(\mathsf P,L,R,\mathsf S)\\ \hline
 \mathrm I&(0,0,\epsilon)&(1,0)&(0,\epsilon,0)\\
 \mathrm {II}&(\epsilon,0,0)&(0,1)&(\epsilon,0,0).
\end{array}                                                     \tag{2}
\]
Here \(h_L,h_R\) are the total charges on \(L\mathsf S\)
and \(R\mathsf S\). The totals on \(\mathsf PL,\mathsf PR\)
are \(1-h_L,1-h_R\), respectively. The interior link edge
has total charge zero. Each of the two boundary
\(\mathsf P\mathsf S\) occurrences has charge zero.
These statements follow by listing the opposite pairs in (2).

The final column is the order with the poles extreme. It exchanges
slots \(2,3\) in (1), reverses each cell orientation, and changes
the glued faces to \(0,3\). In particular either orientation of
the material wire relative to \(L<R\) is covered by (2).
This exchange will be proved on the actual tensors below.

Put
\[
 x=s_{03}s_{12},\qquad y=s_{01}s_{23},\qquad
 z=s_{02}s_{13},\qquad x^N+y^N=z^N,
\]
\[
 W(t)=\prod_{j=1}^{[t]}\frac{y}{z-xq^j},\qquad
 \bar W(t)=\prod_{j=1}^{[t]}\frac{y}{z-xq^{j-1}}.
                                                               \tag{3}
\]
Both products are periodic and nonzero. The literal normalization
proved in [B] is
\[
                   \rho\bar\rho=\frac{y^N}{N(z-x)}.              \tag{4}
\]
The bar labels the opposite tensor, not a Hermitian adjoint.

## 2. The complete finite contraction

Use the face slots
\((\alpha,\beta,\gamma,\delta)=(\alpha_3,\alpha_1,\alpha_2,\alpha_0)\).
The explicit kernels of [S, (3)] are
\[
\begin{split}
 T(a,c)_{\alpha\beta}^{\gamma\delta}
 &=\rho q^{c(\gamma-\alpha)+\alpha\delta+ac/2+\alpha^2/2}
           W(\gamma-a-\alpha)\delta_{\beta,\gamma+\delta},\\
 \bar T(a',c')_{\gamma\delta}^{\alpha'\beta'}
 &=\bar\rho q^{c'(\gamma-\alpha')-\alpha'\delta-a'c'/2-\alpha'^2/2}
        \bar W(\gamma+a'-\alpha')^{-1}\delta_{\beta',\gamma+\delta}.
\end{split}                                                     \tag{5}
\]
For all the old and reordered charges in (2), \(ac=0\).
Thus these entries also agree exactly with the 1994 operator
convention of [B], whose general conversion is recorded in [S, (22)].

The ball tensor in order (1) is
\[
 Q_{\alpha\beta}^{\alpha'\beta'}
       =\sum_{\gamma,\delta}
          T(a,c)_{\alpha\beta}^{\gamma\delta}
          \bar T(a',c')_{\gamma\delta}^{\alpha'\beta'}.
                                                               \tag{6}
\]
The deltas give \(\beta=\beta'\), leaving one sum. A useful exact
sum, including \(m=0,d\), is
\[
 \sum_tq^{(m+1)t}\frac{W(t)}{\bar W(t-m)}
 =N y^{m-N}(z-x)(-x)^{d-m}q^{m(m+1)/2},
 \qquad 0\le m<N.                                               \tag{7}
\]
Indeed
\[
 \frac{W(t)}{\bar W(t-m)}
  =\frac{y^m(z-x)}{\prod_{j=0}^m(z-xq^{t-j})}.
\]
Complete its denominator to the full cyclic product \(y^N\).
The complementary numerator has degree \(d-m\) in \(q^t\).
After multiplication by \(q^{(m+1)t}\), only its top term
survives. Its coefficient is
\((-x)^{d-m}q^{m(m+1)/2}\), since
\(\sum_{j=1}^{d}j=0\) modulo the odd \(N\). This proves (7)
without a limiting or generic-rank argument.

Let \(n=[\alpha'-\alpha]\), and put \(r=-y/x\).
For case I take \(t=\gamma-\alpha\). The phase left in (6) is
\[
             (n+1)t-n\beta-n(n+1)/2.
\]
Use (7) with \(m=n\), then (4). For case II take
\(t=\gamma-\alpha-\epsilon\). Its phase is
\[
                    nt-n\beta-n(n-1)/2,
\]
and its ratio is \(W(t)/\bar W(t+1-n)\).
Use (7) with \(m=[n-1]\). The exact results are
\[
 Q_{\alpha\beta}^{\alpha'\beta'}=
 x^d q^{-n\beta}\delta_{\beta,\beta'}
 \begin{cases}
 r^n,&\mathrm I,\\
 r^{[n-1]},&\mathrm {II}.
 \end{cases}                                                   \tag{8}
\]
No power of \(N\) or decoration factor has been suppressed.
Before the order exchange this is a difference-to-diagonal
array; it is not yet the paired physical wire.

## 3. The actual paired face permutation

We use the primary face tensor [K, (3.6)], but prove the needed
paired permutation rather than invoking the printed symmetry.
For regular representations \(p,q_0\), let
\(P_0=x_p,Q_0=x_{q_0},D_0=x_{q_0^{-1}p}\), choosing
\(x_{p^{-1}q_0}=-D_0\). Write
\[
 \phi(p,q_0)=
 \frac{\langle P_0,D_0\rangle^{1/2}}
      {N\langle Q_0,-D_0\rangle^{1/2}}
 f\left(0,\frac{P_0}{qD_0}\,\middle|-\frac{D_0}{Q_0}\right),
\quad
 F_{uv}(p,q_0)=\phi(p,q_0)q^{uv},
\quad
 F^{uv}(p,q_0)=\frac{q^{-uv}}{N\phi(p,q_0)}.                     \tag{9}
\]
Here the brackets and finite \(f\) are precisely those of [B].
The scalar is a unit. To see this directly, the cyclic summand
recurrence at first argument zero gives
\[
 f(0,v\mid qz)=\frac{z-1}{qvz}f(0,v\mid z).
\]
At (9), \(v,z\ne0\) and \(z^N\ne1\). A zero would therefore
annihilate all \(N\) Fourier coefficients of the nonzero cyclic
summand, which is impossible. The bracket factors are units as well.
Consequently the displayed upper and lower \(F\)'s are literal
bilinear inverses.

For the old tetrahedron use the primary roots
\[
 (P_0,Q_0,R_0,B_0,C_0,H_0)
 =(s_{01},s_{12},s_{23},s_{02},s_{13},s_{03}).
\]
After exchange \(23\) they are
\((P_0,C_0,-R_0,H_0,Q_0,B_0)\); its Fermat triple is
\((z,-y,x)\). Denote its scalars by \(\rho_{\rm new},\bar\rho_{\rm new}\).
The exact cyclic product identities
\[
 W_{\rm old}(n)\bar W_{\rm new}(-n)=q^{-n(n+1)/2},\qquad
 \bar W_{\rm old}(n)W_{\rm new}(-n)=q^{-n(n-1)/2}                \tag{10}
\]
follow by taking successive ratios and checking \(n=0\).
They include the cyclic endpoints.

For clarity, the full scalar in the positive-cell permutation is
\[
 \Theta=
 \frac{\rho_{\rm old}\phi(q_0,q_0r_0)}
      {\bar\rho_{\rm new}\phi(pq_0,pq_0r_0)}.
\]
Using the 1994 kernels, direct summation gives
\[
\begin{split}
 &\sum_{\beta,\delta}
 T^{94}_{\alpha\beta}{}^{\gamma\delta}(a,c)
 F_{\delta D}(q_0,q_0r_0)F^{\beta B}(pq_0,pq_0r_0)\\
 &\hspace{12mm}=
 \Theta q^{a/4}
 \bar T^{94}_{\rm new,\alpha D}{}^{\gamma B}
                (a,\epsilon-a-c).
\end{split}                                                     \tag{11}
\]
The Fourier sum imposes \(B=\alpha+D\); (10) supplies the
remaining product and quadratic phase. The negative mate has
the inverse placements \(F^{\delta D'},F_{\beta'B'}\), scalar
\[
 \bar\Theta=
 \frac{\bar\rho_{\rm old}\phi(pq_0,pq_0r_0)}
      {\rho_{\rm new}\phi(q_0,q_0r_0)}
\]
and phase \(q^{-a'/4}\). Its new charges are
\((a',\epsilon-a'-c')\), by the second identity in (10).
These equations are obtained from the finite kernels; neither
\(\Theta=1\) nor a published permutation theorem is assumed.

The two internal \(F\)'s cancel on the shared face \(0\).
Moreover (4) for the new triple gives
\[
 \Theta\bar\Theta=
 \frac{y^N/[N(z-x)]}{(-y)^N/[N(x-z)]}=1.                        \tag{12}
\]
In both cases (2), \(a=a'\), so the two phases in (11) cancel.
All old and new \(ac\)'s are zero. Thus the raw two-cell tensor
in the pole-extreme order equals exactly the paired transform
of (8) on its remaining face \(1\):
\[
 Q^F_{\alpha\alpha';BB'}=
 \sum_{\beta,\beta'}Q_{\alpha\beta}^{\alpha'\beta'}
 F^{\beta B}(pq_0,pq_0r_0)F_{\beta'B'}(pq_0,pq_0r_0).
\]
The scalar \(\phi\) cancels, and
\[
 \frac1N\sum_\beta q^{\beta(B'-B-n)}=\delta_{B'-B,n}.
                                                               \tag{13}
\]
This is an actual paired face operation. It is not an arbitrary
physical Fourier change of the cut index.

## 4. The boundary adapters and the exact physical word

Use the common poles \(\mathsf P,\mathsf S\) and root pairs
\[
 (a_L,b_L)=(s_{01},s_{12}),\qquad
 (a_R,b_R)=(s_{03},-s_{23}).
\]
Thus \(x=a_Rb_L\) and \(r=a_Lb_R/(a_Rb_L)\). For either port set
\[
 f_\nu(k)=a_\nu^{[k-1]}b_\nu^{[-k]},\qquad
 \mathcal A_\nu(j)=q^{jk_\nu}f_\nu(k_\nu),\quad \nu=L,R.
                                                               \tag{14}
\]
Specify the ordered boundary faces by
\[
 k_L=\alpha'-\alpha+h_L,\qquad
 k_R=B-B'+h_R.
\]
The opposite order at the two ports is part of the boundary map.
On (13), \(k_L+k_R=1\). The full endpoint-inclusive identities are
\[
\begin{array}{ll}
 f_L([n+1])f_R([-n])=x^d r^n,&\mathrm I,\\
 f_L(n)f_R([1-n])=x^d r^{[n-1]},&\mathrm {II}.
\end{array}                                                     \tag{15}
\]
For case I the endpoint \(n=d\) uses \(f_L(0)=a_L^d\) and
\(f_R(1)=b_R^d\); all other entries are the geometric progression.
For case II the endpoints \(n=0,1\) give respectively
\((a_Lb_R)^d\) and \(x^d\); the remaining entries give the
displayed progression. Thus no cyclic carry was dropped.

Equations (8),(13),(15), followed by the finite Fourier expression
for \(\delta_{k_L+k_R,1}\), prove the all-boundary identity
\[
 \boxed{\quad
 \mathcal Q_{\rm collar}
       =\frac1N\sum_{j=0}^{N-1}q^{-j}
                         \mathcal A_L(j)\mathcal A_R(j).
 \quad}                                                        \tag{16}
\]
The paired adapters are the actual functions of [A]. Their inverse
on their rank-\(N\) images proves that the physical two-leg tensor is
\[
                         K=\frac1N Z^{-1},
 \qquad Z_{ij}=q^i\delta_{ij}.                                 \tag{17}
\]
In particular it is symmetric under exchanging the physical ends.
The two charge recipes, not symmetry alone, prove its use in either
order relative to an oriented material wire.

## 5. Sewing, the material-vertex measure, and the fixed cut

Two oppositely ordered port disks with common roots \(a,b\)
and complementary charges obey the exact bilinear identity [A]
\[
 \sum_{\alpha_-,\alpha_+}
 \mathcal A_h(\alpha_-,\alpha_+;i)
 \mathcal A_{1-h}(\alpha_+,\alpha_-;j)
              =N^2(ab)^d q^i\delta_{ij}.                       \tag{18}
\]
In this gluing the material port vertex becomes one interior
vertex, and its two edges to the poles become non-link edges.
Their actual factors are \(N^{-1}\), \(a^{-d}\), and \(b^{-d}\).
Therefore the normalized joining tensor is exactly
\[
                              S=NZ.                            \tag{19}
\]
The collar has no interior vertex and its only interior edge is
the link edge \(LR\); it contributes no additional non-link weight.
The two boundary pole-edge occurrences remain boundary data.

Inserting the collar in an old port identification replaces one
interior material vertex by two. The corresponding old factor
\(S\) is replaced by two sewings and the literal ball (17):
\[
                      SK=KS=I,\qquad SKS=S.                    \tag{20}
\]
Thus the change of vertex count, the two sets of non-link edge
weights, every decoration factor, and the original wire clock
are all accounted for. This is an equality of boundary tensors.
It holds against arbitrary exterior tensors on the specified
paired images, including the actual crossing arrays of [S].
An arbitrary row on the full face-pair space is restricted to
that image by its exact projector; no Hermitian row is substituted.

The literal planar cut is \(E_{00}\), as proved in [A]. Since
\(K\) and \(S\) are diagonal,
\[
 [K,E_{00}]=[S,E_{00}]=0,\qquad
 SKS E_{00}=S E_{00}=N E_{00}.                                 \tag{21}
\]
The cut can be placed on either side of the inserted neutral collar
without changing its index or replacing it by a uniform state.
In the face-pair realization its transported representative is
\[
 \mathcal E_\nu=\mathcal A_\nu E_{00}\mathcal L_\nu,\qquad
 (\mathcal E_\nu)_{k,k'}
                   =\frac{f_\nu(k)}{N^2f_\nu(k')},              \tag{22}
\]
where the entries in (22) mean full face-pair entries with the
indicated differences. The inverse dual \(\mathcal L_\nu\), including
its \(f_\nu^{-1}\), is the one of [A].

For an oriented crossing diagram one may choose \(h=1\) on incoming
crossing ports and \(h=0\) on outgoing ports. There are two of each,
so the boundary sum is two, as required by [S, (8)]. Every joined
wire has complementary charges. Recipe I or II in (2) selects the
incoming and outgoing ends independently of their global vertex
order. Consequently any finite number of these specified wire
subdivisions preserves the finite paired-boundary contraction
and its prescribed cut by repeated use of (20),(21).
This statement concerns the stated port gluing; it does not assert
a separate identification of a proposed whole triangulation.

All identities are finite holomorphic equalities on the same
regular root domain, so their decoration derivatives retain the
normalizations and inverse rows. No off-root level deformation,
original meridian-normal adapter, positivity, or scalar lower
bound follows. In particular the calculation supplies a material
wire-resolution interface, not the further Hamiltonian detours
through \(\mathsf P,\mathsf S\), a free-vertex deletion, or a
pushforward of a selected geometric integration cycle.

## Complete direct proof sources

- [K] Kashaev, *Quantum Dilogarithm as a 6j-Symbol*,
  hep-th/9411147v2, complete 13-page primary text; only its literal
  definitions and charge/weight conventions are used.
  Local PDF: research_archive/literal-charged-bubble-2026-11-17/kashaev1994.pdf.
  SHA256 dec5ba817a401b1ab88c6db1fbac6b8062c2cea05f19077097de247eca2642bb.
- [B] [Literal charged tetrahedron bubble](research_literal_charged_tetrahedron_bubble.md).
  SHA256 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b.
- [A] [Paired-face boundary adapter](research_kashaev_paired_face_boundary_adapter.md).
  SHA256 c430fd2714acdc7588003e1c18c60453e1ebe123bd7c0155d20a0eef639ec8ed.
- [S] [Nine-cell boundary source](research_nine_tetrahedron_boundary_source_reduction.md).
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.

All four complete direct texts were read and the used implications
checked. No mathematical program, numerical experiment, printed
permutation theorem, or global state-invariance assertion was used.
