# A source reset gives a polynomial vacuum gap at unit parameters

22 November 2026. Research note. Earlier final notes and public
manuscripts remain unchanged.

The actual product of two centered coherent inputs has a bounded
positive annihilator with a simple kernel and gap at least
\(1/(4N^2)\), uniformly on compact unit-angle triangles. The construction
uses a division-free nearest-neighbor equation and one explicit
two-coordinate source reset. It retains the entire coefficient space,
including exact zero blocks and repeated-root coordinates.

The reset uses two finite products from the original source. It is
neither a projector onto a supplied full output vector nor a replacement
for an original closing. This proves one multiplication primitive and
its genuine turn, without asserting closure under arbitrary further
gluings.

## 1. The full source and its cleared coefficients

Use the full algebra and the Newton and centered bases of the
[centered compiler](research_centered_fourier_conway_compiler.md):
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=e^{\pi i d^2/(2N)}.
 \tag{1}
\]
Both bases are orthonormal in the positive Newton coefficient norm.
This is the full \(N\)-dimensional algebra, including value and
first-derivative coordinates at repeated Casimir roots; it is not the
uniform physical Hilbert--Schmidt norm. Write
\[
 Z_N(t)=\sum_{a=0}^d|t|^{2a},\quad
 u_N(t)=Z_N(t)^{-1/2}\sum_{a=0}^dt^af_a,\quad
 w_N(y,z)=u_N(y)u_N(z)=\sum_{j=0}^d b_je_j .
 \tag{2}
\]
Fix a compact subset \(K\) of the open angle triangle
\[
 b>0,\qquad c>0,\qquad b+c<1,\qquad
 y=-e^{-2\pi ib},\quad z=-e^{-2\pi ic}.
 \tag{3}
\]
In particular \(Z_N(y)=Z_N(z)=N\).

The [whole-output formula](research_centered_coherent_product_energy.md)
initially gives \(b_j\) by a ratio of finite products. Canceling its
two complete denominator products gives the polynomial identity
\[
 \boxed{\quad
 b_j=\frac{\kappa^2(-q)^j}{N^2}
 (Q;Q)_j(Qyz;Q)_j
 (-qQ^{j+1}y;Q)_{d-j}(-qQ^{j+1}z;Q)_{d-j}.
 \quad}
 \tag{4}
\]
Here \((a;Q)_r=\prod_{h=0}^{r-1}(1-aQ^h)\).
Indeed \(D_N(t)=1-\eta t^N=(-qt;Q)_N\), so the cancellation
holds in the open bidisk for the unnormalized product
\(U_N(y)U_N(z)\), where \(U_N(t)=\sum_{a=0}^dt^af_a\).
Its coefficient formula is polynomial, with prefactor
\(\kappa^2(-q)^j/N\), and extends to the unit parameters.
Dividing that product by \(N\) there gives (4). No limiting ratio
\(0/0\) is used. All complex carrier factors are retained.

## 2. The incoming lines also have a polynomial gap

In centered coordinates put
\[
 (\mathsf B_t x)_a=x_{a+1}-t x_a,\qquad 0\le a<d .
 \tag{5}
\]
Its kernel is exactly \(\mathbb C u_N(t)\).
After a diagonal phase conjugation, the eigenvectors of
\(\mathsf B_t\mathsf B_t^*\) are the Dirichlet sine vectors.
Its eigenvalues are
\[
 1+|t|^2-2|t|\cos(\ell\pi/N),\qquad 1\le\ell<N.
 \tag{6}
\]
For every \(|t|\le1\) their minimum is at least
\(\sin^2(\pi/N)\ge4/N^2\), since the smallest expression equals
\((|t|-\cos(\pi/N))^2+\sin^2(\pi/N)\).
Their maximum is at most \(4\).
Consequently, if \(P_t\) denotes the orthogonal projection onto the
input line, then
\[
 \mathsf B_y^*\mathsf B_y\otimes I+
 I\otimes\mathsf B_z^*\mathsf B_z
 \ \ge\ \frac4{N^2}(I-P_y\otimes P_z).
 \tag{7}
\]
The product line in (7) is mapped by the original multiplication to
the nonzero output line constructed below.

## 3. A nonsingular local equation and two crossing points

Define, for \(0\le j<d\), \(v_j=Q^{j+1}\) and
\[
 a_j=(1+qyv_j)(1+qzv_j),\qquad
 n_j=-q(1-v_j)(1-yzv_j),\qquad
 \nu_j=(|a_j|^2+|n_j|^2)^{1/2}.
 \tag{8}
\]
The cleared source satisfies \(a_jb_{j+1}=n_jb_j\), including
every exact zero. For all sufficiently large \(N\), uniformly on
\(K\), \(\nu_j\) is bounded below by a positive constant.
To see this on the whole unit circle, the limiting zeros of \(a\)
occur at angles \(b,c\), and those of \(n\) at \(0,b+c\).
These sets are disjoint with uniform separation on \(K\).
The factor \(q\) changes the former angles by only \(1/(2N)\).

Thus the following rows have no singular division at a source zero:
\[
 (\mathsf A_Nx)_j=\frac{a_jx_{j+1}-n_jx_j}{\nu_j},
                         \qquad 0\le j<d .
 \tag{9}
\]
Each row has Euclidean norm one and involves adjacent coordinates.
Rowwise Cauchy--Schwarz and summation give
\(\|\mathsf A_N\|^2\le2\).

The signs of the finite squared ratios are controlled without dividing
by \(a_j\). On the unit circle define
\[
 F_N(u)=|(1-v)(1-yzv)|^2
       -|(1+qyv)(1+qzv)|^2,\qquad v=e^{2\pi iu}.
 \tag{10}
\]
This is a real trigonometric polynomial of degree at most two.
Uniformly on \(K\), it is \(C^1\)-close by \(O_K(N^{-1})\) to
\[
 F_\infty(u)=16\sin(\pi b)\sin(\pi c)
 \left[\cos(2\pi u-\pi(b+c))-\cos(\pi b)\cos(\pi c)\right].
 \tag{11}
\]
For verification, put
\(A=\sin(\pi u)\sin(\pi(u-b-c))\) and
\(B=\sin(\pi(u-b))\sin(\pi(u-c))\).
Then \(A-B=-\sin(\pi b)\sin(\pi c)\), and
\(A+B=\cos(\pi b)\cos(\pi c)-\cos(2\pi u-\pi(b+c))\).
Equation (11) follows from \(16(A^2-B^2)\).

Set
\[
 \omega=\pi^{-1}\arccos(\cos(\pi b)\cos(\pi c)),\qquad
 u_\pm=\frac{b+c\pm\omega}{2}.
 \tag{12}
\]
Since \(|b-c|<\omega<b+c\),
\[
 0<u_-<\min(b,c)\le\max(b,c)<u_+<b+c<1.
 \tag{13}
\]
The two roots are simple. Their separation, their derivative magnitudes,
and all strict margins in (13) are uniform on \(K\).
The \(C^1\) estimate therefore gives exactly two simple finite roots
\(u_-^N,u_+^N\), with the same ordering and \(O_K(N^{-1})\)
displacements. The sign of \(F_N\) is positive between them and
negative outside. This follows by preserving derivative signs in two
small root neighborhoods and the nonzero sign on their complement.
Define the explicit interior peak index
\[
                         k=\lfloor Nu_+^N\rfloor .
 \tag{14}
\]
An exact grid crossing can give two tied adjacent peaks; (14) chooses
one. The uniform margins give \(1\le k<d\) for large \(N\).
The equation determining this index has fixed degree: multiplying
the Laurent polynomial in (10) by \(v^2\) gives degree at most four.

## 4. The exact zero blocks and the one source reset

All factors \((Q;Q)_j\), \(j<N\), are nonzero. A tail factor
in (4) vanishes precisely at a half-grid relation
\(r_b=Nb-\tfrac12\in\mathbb Z\) or
\(r_c=Nc-\tfrac12\in\mathbb Z\).
Such an index lies in \(\{0,\ldots,d\}\).
Define \(L\) as the maximum of \(0\) and the root indices that
exist. Define \(U=d\), except that if \(s=N(b+c)\) is an
integer, put \(U=s-1\). Formula (4) proves
\[
 b_j\ne0\ \Longleftrightarrow\ L\le j\le U,\qquad
                         S=\{L,\ldots,U\}.
 \tag{15}
\]
The strict root margins show, for large \(N\), that \(k\in S\).
If \(L>0\), then \(L/N\) lies strictly between the two crossings.
If \(U<d\), then \((U+1)/N\) lies strictly after the upper
crossing. In particular \(b_k\ne0\), so the following finite source
expression is defined:
\[
 \mathsf C_Nx=
       \frac{b_kx_0-b_0x_k}{\sqrt{|b_k|^2+|b_0|^2}},\qquad
 \mathsf H_N=\mathsf A_N^*\mathsf A_N+
                           \mathsf C_N^*\mathsf C_N .
 \tag{16}
\]
Only the two explicit products (4) at \(0,k\) enter this reset.
Their common normalization cancels. No unknown invariant, full-state
projector, or division by a possibly zero endpoint is involved.
The complex coefficients, rather than just their moduli, are essential.
The reset has norm one. We have
\[
 \mathsf H_Nw_N=0,\qquad 0\le\mathsf H_N\le3I.
 \tag{17}
\]
When \(b_0=0\), the reset is a unit phase times the coordinate
\(x_0\). It then pins a zero-source coordinate rather than coupling
it to the active support.

## 5. Coercivity on the nonzero support

Write \(\mu_j=|b_j|^2\) on \(S\), and \(x_j=b_jg_j\).
On an edge lying in \(S\), equation (9) contributes
\[
 |(\mathsf A_Nx)_j|^2
 =\frac{\mu_j\mu_{j+1}}{\mu_j+\mu_{j+1}}
                          |g_{j+1}-g_j|^2 .
 \tag{18}
\]
Its conductance is at least
\(\tfrac12\min(\mu_j,\mu_{j+1})\).
If \(L=0\), the reset has the same formula for the edge \(0,k\).
The sign pattern of (10) says that the weights first decrease to a
valley, increase to \(k\), and then decrease. If \(L>0\), the
initial valley has already been removed by the actual zero prefix,
so the active weights have only the one peak \(k\).

If \(L=0\), choose as anchor whichever of \(0,k\) has the larger
weight. From any index first follow increasing weights to its local
maximum, and, if necessary, cross the reset to the larger maximum.
If \(L>0\), simply ascend to \(k\). Tied steps cause no problem.
Every path has at most \(N+1\) edges, and every conductance on it is
at least half its starting weight. Weighted Cauchy--Schwarz gives,
for any \(x\) supported on \(S\) and orthogonal to \(w_N\),
\[
 \|x\|^2\le2N(N+1)
       \left(\|\mathsf A_Nx\|^2+|\mathsf C_Nx|^2\right).
 \tag{19}
\]
Indeed \(\sum_S\mu_jg_j=0\), so its weighted variance is no larger
than the squared distance to the value at the chosen anchor.
For each starting vertex its anchored squared difference, multiplied
by its weight, is at most \(2(N+1)\) times the total edge energy.
Summing over at most \(N\) vertices proves (19). No lower bound on
the smallest nonzero coefficient is used.

## 6. Coercivity on the zero blocks

The zero coordinates are retained and need no extra projector.
At a denominator root \(a_j=0\), its row is a unit phase times
\(x_j\). At a numerator root \(n_j=0\), its row is a unit phase
times \(x_{j+1}\). Thus every interface between \(S\) and its
complement acts only on the zero side. Rows internal to \(S\) act
only on \(S\); all other rows act only on its complement.
The reset has the same separation, by the observation after (17).
The quadratic energy therefore splits orthogonally into these two
coordinate blocks.

For the zero block use the elementary stable inequalities
\[
 \begin{array}{ll}
 |x_{j+1}|\le |x_j|+\sqrt2|(\mathsf A_Nx)_j|,
                                      &|n_j|\le|a_j|,\\
 |x_j|\le |x_{j+1}|+\sqrt2|(\mathsf A_Nx)_j|,
                                      &|a_j|\le|n_j|.
 \end{array}
 \tag{20}
\]
The divisor in the chosen direction is at least \(1/\sqrt2\)
after normalization. These inequalities apply between the exact
root rows, which instead supply coordinate penalties.

If a zero prefix is present, the reset pins \(x_0\).
The first denominator-root row pins the right end of its first
segment. That segment has one valley; propagate forward from \(0\)
on its decreasing part and backward from its right end on its
increasing part. Any further segment between distinct denominator
roots lies wholly between the two crossings, so propagate backward
from its pinned right endpoint. Repeated denominator roots produce
no additional segment. Finally, a zero tail begins at a numerator
root after \(u_+^N\); it is decreasing and its first coordinate is
pinned by that root row, so propagate forward.

Every zero coordinate consequently has a stable path of length less
than \(N\) from a coordinate penalty. Iterating (20) expresses it
as an anchor, with coefficient of modulus at most one, plus row
errors with coefficients of modulus at most \(\sqrt2\).
Cauchy--Schwarz, then summation over the zero coordinates, gives
\[
 \|x\|^2\le2N^2
       \left(\|\mathsf A_Nx\|^2+|\mathsf C_Nx|^2\right)
                    \qquad(\operatorname{supp}x\subset S^c).
 \tag{21}
\]
The argument includes exact simultaneous half-grid and product-root
collisions. It uses the source's zero pattern, not a quotient that
discards those directions.

## 7. The full gap, the turn, and the original closing

Combining the block splitting with (19)--(21) proves, uniformly on
\(K\) for \(N\ge N_K\),
\[
 \boxed{\quad
 \ker\mathsf H_N=\mathbb Cw_N,\qquad
 \frac1{4N^2}(I-P_{w_N})\le\mathsf H_N\le3I .
 \quad}
 \tag{22}
\]
Here \(P_{w_N}\) is only the orthogonal projection occurring in
the conclusion; it is not used to construct the operator.
The harmless constant follows from \(2N(N+1)\le4N^2\).
For every vector the resulting direction certificate is
\[
 \operatorname{dist}(x,\mathbb Cw_N)
 \le2N\sqrt{\|\mathsf A_Nx\|^2+|\mathsf C_Nx|^2}.
 \tag{23}
\]
The original turn \(J\) is unitary and involutive in this metric.
Thus \(J\mathsf H_NJ\) has kernel \(\mathbb CJw_N\) and the same
gap. The input lines in (7), the original multiplication, and the
output line in (22) are all literal full-source objects.

The reset is additional annihilator data. It changes neither that
multiplication nor any original cup, cap, phase, or scalar observation.
For example the original closing remains exactly
\[
 \phi(w_N)=b_d=\frac{1-(yz)^N}{N(1-yz)} .
 \tag{24}
\]

## 8. A fixed tridiagonal operator selects the source direction

The [single-leg source theorem](research_single_leg_radial_turn_source.md)
removes the exact reset from an approximate direction construction.
For the same compact angle triangle choose
\(a=1-b-c+\tfrac12\min(b,c)\). This is the midpoint between
\(1-b-c\) and \(\min(1-b,1-c)\); the resulting strict prism
shapes form a compact family. Its zero-radius estimate gives
\[
 |\mathcal C_N(0,y,z)|\ge c_K e^{N\delta_K},\qquad
 \delta_K=\min_K[J_0(b+c)-J_0(b)-J_0(c)]>0,
 \tag{25}
\]
where \(J_0(t)=\int_0^t\log(2\sin(\pi u))\,du\).
The original centered functional \(v\mapsto\phi(f_0v)\) has norm
one, and its value on the normalized product is
\(\mathcal C_N(0,y,z)/N\). Also the exact source formula gives
\[
 \|w_N\|\ge\frac{|\mathcal C_N(0,y,z)|}{N},\qquad
 |b_0|=\left|\frac{\kappa^2D_N(y)D_N(z)}
                 {N^2(1+qy)(1+qz)}\right|\le C_KN^{-2}.
 \tag{26}
\]
Here the endpoint denominators have a uniform positive lower bound.
The two-maximum profile on the active support implies
\(\max_j|b_j|=\max(|b_0|,|b_k|)\). Equations (25)--(26)
therefore force \(k\) to be a global peak for large \(N\), and
\[
 |b_k|\ge\|w_N\|/\sqrt N,\qquad
 |r_N|:=|b_0/b_k|\le C_K e^{-N\delta_K}.
 \tag{27}
\]
Now construct, without using either source coefficient in (27),
\[
 \mathsf H_N^0=\mathsf A_N^*\mathsf A_N+
                                      |e_0\rangle\langle e_0|.
 \tag{28}
\]
This is a known tridiagonal positive matrix with a fixed endpoint
pin. Its coefficients depend smoothly on the two real angles,
including exact source resonances. In the \(0,k\) coordinate plane
the difference between its pin and the normalized reset projection
has eigenvalues
\(\pm |b_0|/\sqrt{|b_k|^2+|b_0|^2}\).
It follows that
\[
 \|\mathsf H_N^0-\mathsf H_N\|
 =\frac{|b_0|}{\sqrt{|b_k|^2+|b_0|^2}}
 \le |r_N|.
 \tag{29}
\]
List its eigenvalues as \(\lambda_{0,N}\le\lambda_{1,N}\le\cdots\).
The variational eigenvalue characterization, (22), and (27) give,
uniformly on \(K\) for large \(N\),
\[
 0\le\lambda_{0,N}
 \le\frac{|b_0|^2}{\|w_N\|^2}\le C_K e^{-2N\delta_K},
 \qquad \lambda_{1,N}\ge\frac1{8N^2}.
 \tag{30}
\]
Thus its lowest eigenline is simple; denote its orthogonal projection
by \(P_N^{\mathrm{vac}}\). This line is constructed from (28),
not from the full source vector. Since
\(\mathsf H_N^0 w_N=b_0e_0\), inversion on its orthogonal
complement proves the absolute estimate
\[
 \boxed{\quad
 \|(I-P_N^{\mathrm{vac}})w_N\|
       \le8N^2|b_0|\le C_K .
 \quad}
 \tag{31}
\]
If \(b_0=0\), the selected line is the exact source line.
For any linear row \(\ell_N\) of polynomial dual norm, the error
in \(\ell_N(P_N^{\mathrm{vac}}w_N)\) is polynomial. Consequently
it is relatively exponentially small whenever the original
\(\ell_N(w_N)\) has a positive exponential lower rate.

One explicit coefficient also fixes the source scale constructively.
Choose any unit vector \(v_N\) on the lowest eigenline. Write
\(w_N=\alpha_Nv_N+e_N\), where \(\|e_N\|\le C_K\) by (31).
Since \(|b_k|\ge\|w_N\|/\sqrt N\), (25)--(26) imply
\[
 |v_{N,k}|\ge\frac1{2\sqrt N},\qquad
 \widehat w_N=\frac{b_k}{v_{N,k}}v_N,\qquad
 \|\widehat w_N-w_N\|\le C_K(1+2\sqrt N)
 \tag{32}
\]
for large \(N\). For the first inequality use
\(|\alpha_Nv_{N,k}|\ge|b_k|-C_K\) and
\(|\alpha_N|\le\|w_N\|\). For the last, subtract the two vectors:
the difference is \((e_{N,k}/v_{N,k})v_N-e_N\).
The definition is invariant under the phase chosen for \(v_N\).
Thus the tridiagonal operator and the single known finite product
\(b_k\) construct a full source-scaled approximation; no unknown
packet norm or original knot scalar enters it.

For a compact strict prism family extending the input angles, put
\(x_r=-r e^{-2\pi ia}\). Both coherent rows
\(v\mapsto\phi(vu_N(x_r))\) and
\(v\mapsto\phi(Jv\,u_N(\bar x_r))\) have dual norm one.
The single-leg theorem gives their actual values on \(w_N\) modulus
at least \(c e^{N\delta}/N^{3/2}\), uniformly on compact strict
prism families and \(0\le r\le1\). Replacing \(w_N\) by
\(\widehat w_N\) in either row therefore changes the value by a
relative error at most \(C N^2e^{-N\delta}\).

## 9. Scope and complete proof sources

The original closing (24) can vanish on the displayed triangle.
A polynomial vacuum gap does not replace it by a norm or prove
a lower scalar overlap. The errors (31)--(32) do not guarantee
accuracy for a bounded original cap whose value is small or zero,
or for an arbitrary exterior whose dual norm is exponential.
No parameter differentiability of the chosen index or exact reset
is asserted. The fixed operator (28) avoids those choices, without
identifying its line with a supplied classical shape or proving
arbitrary short-word transport or further binary closure.
No new knot-volume class or finite-exception theorem follows here.

The complete direct proof sources are:

| Source | SHA-256 |
|---|---|
| [Whole coherent-product energy, 393 lines](research_centered_coherent_product_energy.md) | 73152328a77ba5d63a2a8eaa17647ed38b7683c613e0947e3bda9e451dda76e2 |
| [Full centered compiler, 405 lines](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Single-leg initialized source, 326 lines](research_single_leg_radial_turn_source.md) | c624e0edbaadb57279c00420d3f552e93c67cb84972926aad27ff51c2c973e7e |

All three complete texts were read at the matching pins. The cleared
unit-parameter support calculation, the nonsingular source reset,
the weighted and stable-path proofs, and the fixed-boundary
spectral comparison are given above. Orthogonal line selection is
the conclusion, not an assumed geometric packet.
Only written mathematics and text operations were used.
