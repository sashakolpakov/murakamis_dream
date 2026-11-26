# The integral clock coupling and its finite Gaussian transform

Written deduction, 15 November 2026. We use the complete original
singleton incidence sum, including every closing degree and pivotal
phase. For a braid whose closure is a knot, its quadratic phase has an
integral normal form governed by the Alexander polynomial at \(-1\).
This gives an exact Fourier reduction at every level. No coprimality
assumption, numerical calculation, or change of the closing functional
is used.

The nonzero Gaussian coefficients obtained below have polynomial size.
This controls those coefficients, not the coherent sum in which they
occur. In particular it supplies no volume lower bound.

## 1. The original lattice and its midpoint map

Let the signed braid have \(b\) heads and \(c\) crossings, with knot
closure \(K\). Put \(d=N-1\), \(q=e^{\pi i/N}\), and
\(S_a=\prod_{r=1}^a2\sin(\pi r/N)\), with \(S_0=1\).
Use the physical signs \(\sigma_j\) of the joint-phase source.
At crossing \(j\), the overstrand goes from \(u_j+v_j\) to \(v_j\),
and the understrand goes from \(J_j\) to \(J_j+u_j\). Its four
incidences are
\[
 (d-u_j-v_j,\ u_j-h_j+v_j,\ h_j-v_j,\ v_j).
 \tag{1}
\]
The closing row on head \(i\) is \((d-a_i,a_i)\). The linear wire
conservation equations are precisely those in the joint-phase note,
Section 2. Let \(P\) be their integral solution lattice in the physical
variables \(u,v,a\), without the inequalities. Every \(J_j\) is its
actual integral prefix function. Define
\[
 \mathcal M:P\longrightarrow\mathbb Z^c,
 \qquad \mathcal M_j(p)=u_j+2J_j.
 \tag{2}
\]
Thus \(\mathcal M_j\) is the sum of the two understrand degrees.

The homogeneous incidence lattice is integrally isomorphic to
\(P\oplus\mathbb Z^c\), the second factor consisting of the clocks
\(h_j\). Indeed (1) and the closing pairs reconstruct all incidence
variations; conversely \(v_j=n_{j3}\), \(h_j=n_{j2}+n_{j3}\),
\(u_j=n_{j1}+n_{j2}\), and the closing indices recover the inverse.
There is no divisibility condition in this change of coordinates.

The affine source fiber has the integral base point with all physical
degrees and clocks zero. Its first incidence in each event is \(d\),
and all its other incidences are zero. Consequently every source state
is this base point plus a unique element of \(P\oplus\mathbb Z^c\).
The inequalities \(0\le n_e\le d\) still specify exactly which such
elements occur.

The full variable-dependent phase is
\[
 \Phi_N(p,h)=
 \sum_j\sigma_jh_j\mathcal M_j(p)
 +\sum_j(N+\sigma_j)h_j
 -d\sum_j\sigma_jJ_j(p)-2\sum_{i=2}^b a_i(p).
 \tag{3}
\]
In particular its quadratic part is a pairing of clocks with physical
flows. It has no clock--clock or physical--physical term.

## 2. An integral exact sequence

Write \(y\in\mathbb Z^b\) for the initial head degrees and
\(t_j=\mathcal M_j(p)\). At a positive crossing on adjacent heads,
the checked output degrees are
\[
 \binom{t-J}{I+2J-t}
 =M_+\binom I J+v_+t,
 \quad M_+=\begin{pmatrix}0&-1\\1&2\end{pmatrix},
 \quad v_+=\binom1{-1}.
 \tag{4}
\]
For a negative crossing the input order is \((J,I)\), and the output is
\[
 \binom{I+2J-t}{t-J}
 =M_-\binom J I+v_-t,
 \quad M_-=\begin{pmatrix}2&1\\-1&0\end{pmatrix}=M_+^{-1},
 \quad v_-=-v_+.
 \tag{5}
\]
These are direct consequences of transfer conservation and
\(u=t-2J\); they do not impose a new coloring on the source.
Embed these matrices and vectors at each crossing's two heads and put
\[
 B=M_c\cdots M_1,\qquad
 D_j=M_c\cdots M_{j+1}v_j.
 \tag{6}
\]
Every matrix preserves the sum of the head degrees. Write
\(\mathbb Z_0^b=\{y:\sum_i y_i=0\}\). Closing the braid gives the
integral identification
\[
 P=\{(y,t)\in\mathbb Z^b\oplus\mathbb Z^c:
                    (I-B)y=Dt\},
 \qquad \mathcal M(y,t)=t.
 \tag{7}
\]
The inverse follows the crossings in order, using \(u=t-2J\).

The columns of \(D\) span \(\mathbb Z_0^b\). To check this integrally,
\(\operatorname{im}(M_j-I)\subset\mathbb Z v_j\). It follows that
\(D_j-v_j\) is an integral combination of the later raw vectors
\(v_{j+1},\ldots,v_c\). Descending induction therefore proves that
the propagated and raw columns have the same integral span. The raw
vectors are signed adjacent simple roots. The graph of the adjacent
heads occurring in a knot braid is connected: otherwise its braid
permutation would preserve two nonempty sets, whereas that permutation
is one cycle. The simple roots on this connected graph span
\(\mathbb Z_0^b\).

Consequently (7) gives the exact sequence
\[
 0\longrightarrow\ker(I-B)\longrightarrow P
   \xrightarrow{\mathcal M}\mathbb Z^c
   \xrightarrow{\ t\mapsto[Dt]\ }
       \mathbb Z_0^b/(I-B)\mathbb Z^b\longrightarrow0.
 \tag{8}
\]
This also proves \(\operatorname{rank}P=c+1\): the map
\((I-B,-D):\mathbb Z^{b+c}\to\mathbb Z_0^b\) is surjective.

## 3. The Alexander group in the cokernel

Conjugate the head coordinates by
\(E=\operatorname{diag}(1,-1,1,-1,\ldots)\). The local matrices in
(4)--(5) become, respectively, the inverse and the value at \(t=-1\)
of the unreduced Burau block
\[
 T(t)=\begin{pmatrix}1-t&t\\1&0\end{pmatrix}.
 \tag{9}
\]
Thus \(EBE^{-1}\) is the Burau matrix at \(-1\) for the braid with
crossing signs reversed, using the same product convention. Its closure
is the mirror of \(K\); this does not change
\(|\Delta_K(-1)|\).

Here is the minor argument, including the issue at even braid width.
Over \(R=\mathbb Z[t,t^{-1}]\), the unreduced braid matrix
\(\mathcal B(t)\) fixes the column \(\mathbf1\) and the row
\(v(t)=(1,t,\ldots,t^{b-1})\). At \(t=1\) it is the permutation
of a single cycle, so \(I-\mathcal B(t)\) has rank \(b-1\) over
\(\mathbb Q(t)\). Its adjugate is therefore
\[
 \operatorname{adj}(I-\mathcal B(t))
                  =f(t)\,\mathbf1\,v(t),\qquad f(t)\in R.
 \tag{10}
\]
The coefficient is Laurent polynomial because the first entry of
both null vectors is one. All deleted minors are consequently
\(f(t)\) times a signed Laurent unit.

To identify \(f\), use the braid presentation
\(\langle x_1,\ldots,x_b:\beta(x_i)=x_i\rangle\) of the mirror
knot group. The Artin automorphism preserves \(x_1\cdots x_b\);
one of these relations follows from the other \(b-1\). Abelian Fox
differentiation gives \(\mathcal B(t)-I\), up to the transpose and
Laurent basis changes fixed by the action convention. The boundary
map of the infinite cyclic cover is \((t-1)\mathbf1^T\).
Its kernel is free with basis \(e_i-e_b\), \(i<b\). Expressing the
remaining relation boundaries in this basis amounts to deleting one
generator coordinate from the Fox matrix. The resulting square
matrix presents the Alexander module; its determinant is the Alexander
polynomial up to a Laurent unit. This is one of the minors in (10).
Hence \(f(t)\) is \(\Delta_K(t)\), with the mirror convention,
up to such a unit.

At \(t=1\) a deleted minor of the single-cycle permutation matrix
has value \(\pm1\). Thus \(f(-1)\equiv f(1)\pmod2\) is odd and
nonzero. In particular \(I-B\) has rank \(b-1\). Its right kernel
is the primitive alternating vector
\(\varepsilon=(1,-1,\ldots)^T\), and its left kernel is
\(\mathbf1^T\). Deleting one output coordinate identifies
\(\mathbb Z_0^b\) with \(\mathbb Z^{b-1}\). The maximal minors of
the resulting \((b-1)\)-by-\(b\) matrix are precisely the specialized
cofactors; each has absolute value \(|f(-1)|\). Their greatest common
divisor is the index of its image. Therefore
\[
 \left|\mathbb Z_0^b/(I-B)\mathbb Z^b\right|
                         =|\Delta_K(-1)|.
 \tag{11}
\]
No division by \(1+t+\cdots+t^{b-1}\) occurs. In particular the
argument remains valid when \(b\) is even. This is an integral
cokernel statement, rather than a specialization of a rational
rank computation.

The finite group, not only its order, has an Alexander description.
The column dependence of \(I-B\) has coefficients
\(\varepsilon_i=\pm1\). After deleting one output coordinate, any
one input column is therefore an integral combination of the other
columns. Deleting it leaves exactly the same image lattice. The
resulting square matrix is the specialized Alexander presentation
above, up to integral basis changes and possibly a transpose. A
square matrix and its transpose have the same integer Smith factors.
Consequently, as an abstract finite abelian group,
\[
 \operatorname{coker}\mathcal M\cong
     \mathcal A_K/(t+1)\mathcal A_K,
 \tag{11a}
\]
where \(\mathcal A_K\) is the Alexander module. The mirror convention
replaces \(t\) by \(t^{-1}\), which has the same specialization at
\(-1\). This is an abstract isomorphism; no canonical identification
with a transposed presentation is asserted.

Combining (8)--(11), the midpoint map has rank \(c\), a primitive
rank-one kernel, and a finite cokernel of odd order. Let its nonzero
Smith factors be \(s_1\mid\cdots\mid s_c\), all positive. Then
\[
                  \prod_{j=1}^c s_j=|\Delta_K(-1)|.
 \tag{12}
\]
Their nonunit members are independent of the braid presentation by
(11a); the number of unit factors changes with the number of crossings.
For \(b=1,c=0\), the braid is empty. The same assertions use the
empty product one, \(P=\mathbb Z\), and the zero midpoint map.

## 4. Integral hyperbolic form of the actual phase

The kernel generator with initial heads \(\varepsilon\) has
\(a_1=1\). Therefore \(P=\ker(a_1)\oplus\mathbb Z\varepsilon\),
and the image of \(\mathcal M|_{\ker(a_1)}\) is the full image of
\(\mathcal M\). Choose its Smith bases on this complement. Changing
the physical basis
and making the dual integral change in the clocks, with their signs
\(\sigma_j\) absorbed, transforms the quadratic term in (3) into
\(\sum_j s_j x_jy_j\). Choose the remaining physical coordinate
\(z\) to be the primitive kernel direction with initial heads
\(\varepsilon\); with this choice, \(z=a_1\) exactly.
All these changes are unimodular on the integral
incidence lattice. Thus the complete phase, including its linear
terms, is exactly
\[
 \Phi_N=\sum_{j=1}^c
       (s_jx_jy_j+\alpha_{j,N}x_j+\beta_{j,N}y_j)
                              +\gamma_Nz.
 \tag{13}
\]
The displayed coefficients are the transformed integer linear
coefficients of (3), and are affine functions of \(N\). No phase
has been absorbed into an unspecified normalization. Equivalently,
the symmetric quadratic matrix is integrally congruent to
\(\bigoplus_j\left(\begin{smallmatrix}0&s_j\\s_j&0\end{smallmatrix}\right)
\oplus(0)\). Its rank is \(2c\).

The linear term along the free direction can be read without finding
the other Smith coordinates:
\[
 \gamma_N=-d\sum_j\sigma_jJ_j(\varepsilon)
                          -2\sum_{i=2}^b\varepsilon_i.
 \tag{14}
\]
Indeed the zero-midpoint transport fixes \(\varepsilon\) at every
horizontal slice, and its clocks do not vary. If crossing \(j\)
uses heads \(i_j,i_j+1\), then
\(\sigma_jJ_j(\varepsilon)=-(-1)^{i_j-1}\). Consequently
\[
 \gamma_N=(N-1)\sum_j(-1)^{i_j-1}
                       +2\mathbf1_{b\ {\rm even}}.
 \tag{15}
\]
This is one explicit place where the prescribed closing pivots enter
the Fourier support. Dropping them changes the finite transform.

## 5. The complete finite Gaussian transform

Put \(m=2N\), \(e_m(t)=e^{2\pi it/m}\), and
\(G_m=(\mathbb Z/m)^{2c+1}\), in the coordinates \((x,y,z)\) of
(13). This phase is periodic modulo \(m\). Define its normalized
Fourier coefficients by
\[
 g_N(k)=m^{-(2c+1)}\sum_{w\in G_m}
                         e_m(\Phi_N(w)-k\cdot w).
 \tag{16}
\]
For \(r_j=\gcd(m,s_j)=\gcd(N,s_j)\), these coefficients vanish
unless
\[
 k_z\equiv\gamma_N\pmod m,\qquad
 k_{x_j}\equiv\alpha_{j,N}\pmod{r_j},\qquad
 k_{y_j}\equiv\beta_{j,N}\pmod{r_j}.
 \tag{17}
\]
On exactly this affine set, choose any solution
\(y_j^*\) of \(s_jy_j^*\equiv k_{x_j}-\alpha_{j,N}\pmod m\).
Then the exact coefficient is
\[
 g_N(k)=\prod_{j=1}^c\frac{r_j}{m}\,
            e_m\!\left(\sum_j(\beta_{j,N}-k_{y_j})y_j^*\right).
 \tag{18}
\]
The expression is independent of the choices of \(y_j^*\).

For proof, the sum in \(z\) gives the first condition in (17).
Summing in \(x_j\) gives zero unless
\(s_jy_j+\alpha_{j,N}-k_{x_j}\equiv0\). That congruence has
\(r_j\) solutions when the second condition holds. They differ by
\(m/r_j\); summing their remaining characters gives zero unless the
third condition holds, and otherwise gives
\((r_j/m)e_m((\beta_{j,N}-k_{y_j})y_j^*)\). Multiplication proves
(18). This argument also covers even and composite \(N\).

In particular, every admitted coefficient is nonzero, with
\[
 |g_N(k)|=\frac{\prod_j\gcd(N,s_j)}{(2N)^c},\qquad
 (2N)^{-c}\le |g_N(k)|\le
                     |\Delta_K(-1)|(2N)^{-c}.
 \tag{19}
\]
There are \(m^{2c}/\prod_j r_j^2\) admitted frequencies. If
\(N\) is coprime to \(\Delta_K(-1)\), the only support restriction
is the one marked hyperplane \(k_z=\gamma_N\), and every coefficient
there has modulus \((2N)^{-c}\). No assertion of positivity of its
phase is made.

## 6. Exact reduction of the original closing evaluation

Let \(\mathcal W_N\subset\mathbb Z^{2c+1}\) be the coordinates of
the actual feasible incidence states and define
\[
 a_N(w)=\prod_eS_{n_e(w)}^{-1}\quad(w\in\mathcal W_N),
 \qquad
 Z_N(k)=\sum_{w\in\mathcal W_N}a_N(w)e_m(k\cdot w).
 \tag{20}
\]
Every \(a_N(w)\) is positive. Distinct feasible states stay distinct
modulo \(m\): if their coordinate difference were \(m v\), their
incidence difference would be \(m\) times a nonzero integral vector,
whereas each incidence lies between zero and \(N-1<m\). Thus zero
extension to \(G_m\) introduces no aliases.

Fourier inversion of (16) now gives the original source exactly:
\[
 \boxed{\quad
 K_N=\mathcal C_N\sum_{k\text{ satisfying }(17)}g_N(k)Z_N(k),
 \qquad
 \mathcal C_N=\chi_N\kappa^{\sum_j\sigma_j}
                          \eta^{b-1}N^{c+b-1}.
 \quad}                                                     \tag{21}
\]
Here \(\kappa=q^{d^2/2}\), \(\eta=q^{-d^2}\), and \(\chi_N\)
are the original factors. The positive value \(Z_N(0)\) is the
absolute incidence partition whose exponent is the proved concave
angle optimization. It is not substituted for the right side of
(21). Its Fourier evaluations at other frequencies can have phases
and zeros, and the coefficients (18) also have their specified phases.

### Removing the free direction by the actual marked cut

The adopted [marked-cut theorem](research_incidence_marked_cut_observability.md)
gives a further exact reduction. If the incidence sum is weighted by
\(t^{a_1}\), its value is
\[
 F_N(\mathbf1)\,\frac{1+t+\cdots+t^{N-1}}N.
 \tag{22}
\]
This follows from scalarity of the complete pivotal partial trace.
In particular, for every \(0\le r<N\), the sum over all remaining
coordinates at \(a_1=r\) equals \(F_N(\mathbf1)/N\). This is an identity of complete sums;
it is not applied to a fixed clock sector or to a multivariable
fugacity deformation of the exterior.

Our chosen Smith complement makes \(a_1=z\). For any prescribed
integer \(r\) in this range, define the positive slice and its
Fourier evaluations by
\[
 Z_N^r(k_x,k_y)=
 \sum_{(x,y,r)\in\mathcal W_N}
          a_N(x,y,r)e_m(k_x\cdot x+k_y\cdot y).
 \tag{23}
\]
Let \(g_N^0(k_x,k_y)\) be the normalized Fourier transform on
\((\mathbb Z/m)^{2c}\) of (13) restricted to \(z=0\). Its
coefficients are exactly (18), subject only to the two congruences
for each pair in (17). The radical congruence is absent. At \(z=r\)
the additional phase is exactly \(e_m(\gamma_Nr)\); the pair phase
is unchanged. Fourier inversion on this slice, followed by (22), gives
\[
 \boxed{\quad K_N=N\mathcal C_N e_m(\gamma_Nr)
             \sum_{k_x,k_y}g_N^0(k_x,k_y)Z_N^r(k_x,k_y).
             \quad}                                      \tag{24}
\]
All original inequalities and every closing pivot remain in this
formula. The same injection modulo \(m\) proves that the slice has
no aliases. No unknown scalar was divided out, so (24) also holds
when the original invariant vanishes. The choice \(r=r_N\) may depend
on the level; in particular one may choose a central physical degree
instead of the boundary degree zero. No contributing geometric saddle
is inferred for such a chosen slice.

The unweighted \(Z_N^r(0)\) is a different positive partition from
\(Z_N(0)\). For \(r=0\), the condition pins a boundary face and
can force further zero coordinates. The number \(2c\) is the rank
of the ambient integral and Fourier lattice; a feasible slice need
not have that dimension. The unsliced angle maximum cannot be
assigned to an arbitrary prescribed central or boundary slice.

There is, however, an exact choice preserving that positive exponent.
Since \(Z_N(0)=\sum_{r=0}^{N-1}Z_N^r(0)\), choose \(r_N\) attaining
the largest positive slice. Then
\[
          \frac{Z_N(0)}N\le Z_N^{r_N}(0)\le Z_N(0).
 \tag{25}
\]
The already proved exponent of \(Z_N(0)\), namely the maximum of
the concave absolute incidence action, is therefore also the exponent
of this adaptively chosen positive slice. The choice uses positive
weights alone, not the unknown invariant. It need not be a prescribed
central slice or contain the selected complex geometric point.
Equation (25) is not a lower bound for the coherent sum in (24).
What (24) removes exactly is the permanent free direction of the
quadratic phase, using the actual marked cut at any allowed degree.

The older feedback theorem already gives a finite Fourier realization
of the understrand coupling. The additional content here is its
integral normal form on the complete conserved-flow lattice, the
Alexander-controlled torsion, the explicit closing character, and the
nonzero polynomial size of every admitted Gaussian coefficient.
Smith reduction, the Burau--Alexander relation, and finite Fourier
orthogonality themselves are classical methods, not novelty claims.
For coverage of the Burau--Alexander relation see Anthony Conway,
[Burau maps and twisted Alexander polynomials](https://arxiv.org/abs/1510.06678).
Its abstract was checked for coverage; none of its proofs is a premise
of the integral argument above.

The result applies to every fixed knot braid, hence also to a braid
obtained after any fixed short partial filling that gives a knot.
It proves no uniform asymptotic stability under that operation.
The closed Markov identity in the direct source shows why the phases
in (21) remain necessary: complete nonzero-clock sectors can cancel
exactly even though their absolute weights have positive exponential
rate. The Gaussian factors cannot be exponentially small on their
support; the remaining question is the noncancellation of their
prescribed coherent contraction. No nonzero geometric coefficient or
volume limit is inferred here.

## Direct source versions

| Source | SHA-256 |
| --- | --- |
| research_joint_clock_phase_equations.md, Sections 2--4 | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |
| research_incidence_cycle_difference_equations.md, Sections 1--3 | 8d9b4231b2f3a8795b857f361b2054d50a727392457a378a12adb4fe0430e618 |
| closed_braid_period_line.md, Section 5 | cdb5cd8402f17d975a923951d156a6092a9cb5291e8348035fb81623d80f8529 |
| actual_clock_feedback_normal_form.md, Sections 1--3 | f58a4dfd06615ecace95959e58474837f7eb50ef7f01a3c00d517d3938cb06bf |
| research_charged_source_angle_optimization.md, Sections 1--3 | 45b21fabb9cb65512bc3e576eb3d659b6fe14c3dcd90b4164bfdb12b8cedea64 |
| research_charged_variational_markov_loss.md, Sections 2--3 | 5c7e01c1c93d3b399e81b93d2dfff99efea05653c010593d86e1a07a14c11ccb |
| research_incidence_marked_cut_observability.md, Section 1 | c0b9f010a8ab4b69b96bbcb0a32a6b8dad6ed8c39fca1029834f2ba74c13cbfc |
