# A short filling surrounded by repeated zero-filled blocks

Research theorem, 2 November 2026. Fix an actual zero-filled subtree whose
selected original vertices have degree at least three. If sufficiently
many copies meet one original crossing circle, that circle admits every
fixed signed crossing power. The conclusion is a nonzero asymptotic for
the entire boundary polynomial, with a strict bound away from its complete
boundary value. The number of copies required depends on the block, not
on the signed power.

The zero-filled vertices inside the copies can be trivalent and adjacent.
Thus this construction is not a consequence of requiring every selected
vertex of a connected region to have large degree. The estimates below
apply the original trace to the product of the full block polynomials.
They do not apply a crossing matrix to an already estimated remainder.

## 1. The actual block and the exact gluing

Let \(\mathcal B\) be a connected zero-filled subtree satisfying
[the full zero-subtree theorem](research_all_zero_subtree_newton_packet.md).
Write \(b\ge3\) for its number of boundary edges. Distinguish one boundary
angle \(t\), and retain the other \(q=b-1\) angles as the vector
\(\mathbf u\). Its full original boundary polynomial is denoted by
\(F_N(t,\mathbf u)\). It has separate degree at most \(D=N-1\) in
each of \(-2\cos t,-2\cos u_1,\ldots,-2\cos u_q\).

Here and below a zero filling deletes only its original power-zero box.
All intervening turns, disk framings, and full first normal derivatives
remain as in the cited theorem. The algebra is
\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad
 P_N(z)=2T_N(z/2)+2,
\]
where \(T_N\) is the standard Chebyshev polynomial. Its original trace is
\(\phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f\).

The proved block estimates are
\[
 F_N(t,\mathbf u)
 =N^\alpha A(t,\mathbf u)e^{NW(t,\mathbf u)}
                  (1+O(N^{-1})),\qquad
 \alpha=-\frac{3q}{2},                                  \tag{1}
\]
uniformly and holomorphically on a fixed polydisk about zero, and
\[
 |F_N(x+iy,\mathbf a+i\mathbf b)|
 \le C N^p\exp N\left\{
 F_0-c(1-\cos x)-c\sum_{\ell=1}^q(1-\cos a_\ell)
             +C_1y^2+C_1\sum_{\ell=1}^q b_\ell^2\right\}. \tag{2}
\]
The latter estimate holds on the whole real angle torus and a fixed
complex strip. The constants belong to the fixed block. Also,
\[
 W(0,\mathbf0)=F_0,\quad A(0,\mathbf0)>0,\quad
 W_{tt}(0,\mathbf0)=-\kappa<0,\quad
 W_{\mathbf u\mathbf u}(0,\mathbf0)
                         =-\operatorname{diag}(\beta_1,\ldots,\beta_q),
 \quad \beta_\ell>0.                                    \tag{3}
\]
Both \(W\) and \(A\) are separately even, and \(W\) is real on the small
real polydisk. These assertions include the full high-index boundary
terms and both level parities.

Take \(m\) disjoint copies of \(\mathcal B\), and identify only their
distinguished outside vertex with one original circle \(v\). Every
other boundary angle remains independent:
\[
 \mathbf U=(\mathbf u^{(1)},\ldots,\mathbf u^{(m)}).
\]
The resulting selected region is connected; the original degree of
\(v\) is \(m\). Give \(v\) one fixed signed power \(n\in\mathbb Z\).
Its exact boundary polynomial is
\[
 \mathcal P_{m,n,N}(\mathbf U)
 =\phi_N^{(t)}\left[
       R^n\prod_{j=1}^mF_N(t,\mathbf u^{(j)})\right].       \tag{4}
\]
No copy carries an extra \(R^n\). Reduction modulo \(P_N\) occurs in
the original trace, after the product is formed. In particular the
input in (4) may have degree \(mD\); it is not replaced by values at
the distinct roots of \(P_N\).

## 2. The theorem

**Theorem 1.** For every fixed block \(\mathcal B\), there is an integer
\(m_0(\mathcal B)\) such that the following holds for every fixed
\(m\ge m_0(\mathcal B)\) and every fixed signed integer \(n\).

The phase
\[
 \Phi(t,\mathbf U)=
 \sum_{j=1}^m W(t,\mathbf u^{(j)})
                    +\frac{in}{4\pi}t^2-it              \tag{5}
\]
has one critical point \(t=t_*(\mathbf U)\) in a fixed small \(t\)-disk.
It is holomorphic for small complex \(\mathbf U\). At \(\mathbf U=0\),
it is nonzero and lies below the real axis. Put
\[
 \mathcal S(\mathbf U)=\Phi(t_*(\mathbf U),\mathbf U),\quad
 M=\Re\mathcal S(0),\quad
 C_{N,n}=\exp\frac{\pi i n(N-1)^2}{4N}.
\]
Then the entire original polynomial (4) satisfies
\[
 \boxed{\quad
 \mathcal P_{m,n,N}(\mathbf U)
 =C_{N,n}N^{-3(mq-1)/2}\mathcal A(\mathbf U)
       e^{N\mathcal S(\mathbf U)}(1+O_{m,n}(N^{-1})).
 \quad}                                                 \tag{6}
\]
The expansion is uniform and holomorphic on a fixed polydisk.
The amplitude is nonzero there after shrinking it, and is explicitly
\[
 \mathcal A(\mathbf U)=
 i\sqrt{\frac2\pi}\,
 \frac{\sin t_*(\mathbf U)
       \prod_{j=1}^m A(t_*(\mathbf U),\mathbf u^{(j)})}
 {\sqrt{-\sum_jW_{tt}(t_*(\mathbf U),\mathbf u^{(j)})
                                      -in/(2\pi)}}.       \tag{7}
\]
The square root has positive real part at zero and is continued
holomorphically. All fixed parameter derivatives have the same
relative error on smaller polydisks.

There are constants \(c_*,B_*,\varepsilon_*,C_*>0\) and \(p_*\),
which may depend on the fixed \(m,n\), such that
\[
 |\mathcal P_{m,n,N}(\mathbf X+i\mathbf Y)|
 \le C_*N^{p_*}\exp N\left\{
 M-c_*\sum_{\ell=1}^{mq}(1-\cos X_\ell)
                          +B_*\sum_{\ell=1}^{mq}Y_\ell^2\right\},
 \qquad |Y_\ell|<\varepsilon_*.                         \tag{8}
\]
The real angles range over their full periods. The action is separately
even, and its Hessian at zero is diagonal:
\[
 \mathcal S_{u^{(j)}_\ell u^{(k)}_a}(0)
 =\delta_{jk}W_{u_\ell u_a}(t_*(0),\mathbf0)
 =\delta_{jk}\delta_{\ell a}
                      W_{u_\ell u_\ell}(t_*(0),\mathbf0), \tag{9}
\]
with strictly negative real diagonal entries.

The admissibility threshold \(m_0\) is independent of \(n\). The error
constants and the threshold for subsequent fillings need not be.
The statement always fixes \(m,n\) before letting \(N\) tend to infinity.

## 3. Constants that determine a sufficient threshold

This section makes the large-multiplicity assertion checkable from the
already proved block phase and bounds. No extra packet hypothesis is
being imposed on the block.

Choose a small \(r<1/4\) and then a small \(\rho>0\) inside the
holomorphic and positive geometric block charts. On
\[
 |t|\le r,\qquad |u_\ell|\le\rho
\]
put
\[
 Q(t,\mathbf u)=-\frac{W_t(t,\mathbf u)}{\kappa t}.
\]
Evenness removes the apparent singularity at \(t=0\). By (3), the
radii can be chosen so that
\[
 |Q-1|\le\frac1{100},\quad |Q_t|\le L,\quad
 \Re(-W_{tt})\ge\frac\kappa2,\quad
 \Re(-W_{\mathbf u\mathbf u})\ge\beta I,\quad
 \|W_{t\mathbf u}\|\le B|t|,                              \tag{10}
\]
for fixed \(L,B<\infty\) and \(\beta>0\). Matrix inequalities mean
inequalities for real vectors, equivalently for the Hermitian part of
the complex symmetric matrix. The last bound follows from evenness
in \(t\). Choose the chart so that \(A\) has no zero.

Let
\[
 a=\frac r2,\quad c_0=c(1-\cos(a/2)),\quad
 d_0=2\pi\kappa,\quad k_0=\frac{2c}{\pi^2}.
\]
Shrink \(\rho\) further, without changing \(r\), so that throughout
its complex polydisk
\[
 |W(0,\mathbf u)-F_0|\le c_0/4,\qquad
                         C_1q\rho^2\le c_0/4.           \tag{11}
\]
Let
\[
 s_0=1-\cos\rho,\qquad
 K_0=\frac{49C_1}{d_0^2}+\frac{49}{64\pi^2 k_0}.
\]
One sufficient choice is any \(m_0\ge3\) such that, for every
\(m\ge m_0\) and \(D_m=d_0m\),
\[
\begin{gathered}
 D_m\ge 28/r,\qquad
 \frac{2\pi L}{(99/100)^2D_m}<\frac12,\qquad
 D_m^2\ge\frac{196B^2}{\kappa\beta},\\
 \frac{7}{2D_m}<\frac{m c_0}{4},\qquad
 \frac{7}{2D_m}<\frac{m\kappa a^2}{8},\qquad
 \frac{K_0+7/(2d_0)}m<\frac{cs_0}{2}.                   \tag{12}
\end{gathered}
\]
All constants are properties of the one fixed block. Each left side
in the last line decreases with \(m\), whereas the relevant right
sides are positive or increase. Such an integer exists. Enlarging it
to stay inside a prescribed smaller positive geometric chart changes
none of the estimates.

The inequalities in (10)--(12), together with the proved block
estimates, are an explicit verification procedure for a sufficient
threshold. We do not assert that this threshold is close to optimal.

## 4. The critical point and its small action loss

For \(0\le\lambda\le1\), replace the last term of (5) by
\(-i\lambda t\). Write
\[
 \overline Q(t,\mathbf U)=\frac1m\sum_jQ(t,\mathbf u^{(j)}),
 \qquad R_m=(D_m^2+n^2)^{1/2}.
\]
The critical equation is
\[
 t=\frac{-2\pi i\lambda}{D_m\overline Q(t,\mathbf U)-in}. \tag{13}
\]
The denominator has modulus at least \(99R_m/100\). Equations
(10)--(12) make the right side a contraction of \(|t|\le r\) into
\(|t|\le r/4\). Thus it supplies the unique critical point in that
disk, and it varies holomorphically with all the boundary variables.
Moreover,
\[
 |t_\lambda|\le\frac{7\lambda}{R_m},\qquad
 0<-\Im t_\lambda\le\frac{7\lambda D_m}{R_m^2}
                    \quad(\lambda>0).                 \tag{14}
\]
For the sign, write \(\overline Q=a_1+ib_1\). The exact imaginary
part is
\[
 -\Im t_\lambda=
 \frac{2\pi\lambda D_m a_1}
      {|D_m\overline Q-in|^2},
\]
and \(a_1\ge99/100\). These estimates hold even for complex boundary
variables in the chosen polydisk.

Differentiating the stationary value with respect to \(\lambda\)
and integrating proves
\[
 0<
 \sum_j\Re W(0,\mathbf u^{(j)})-\Re\mathcal S(\mathbf U)
 \le\frac{7D_m}{2R_m^2}\le\frac7{2D_m}.                  \tag{15}
\]
In particular \(0<mF_0-M\le7/(2D_m)\). Also
\[
 \Re\Phi_{tt}=\sum_j\Re W_{tt}\le-m\kappa/2.             \tag{16}
\]
Thus the critical point is nondegenerate.

## 5. The complete trace, including its endpoint currents

The physical angles are
\[
 \tau_j=\frac{\pi(N-1-2j)}N,\qquad 0\le j<N.
\]
Choose a genuine midpoint \(a_N=a+O(N^{-1})\), with \(a_N\ge a\).
The original derivative-sampling trace is used at every such point;
its first normals are not discarded.

First remove only the physical angles with \(|\tau_j|\ge a_N\).
For real external angles, (2) bounds the polynomial product there
by a polynomial in \(N\) times
\[
 \exp N\left\{mF_0-mc_0
                       -c\sum_\ell(1-\cos U_\ell)\right\}. \tag{17}
\]
The same rate, with a polynomial factor, bounds its needed derivative
in \(z=-2\cos t\). Indeed apply the ordinary polynomial Markov
inequality on the fixed spectral interval
\([-2\cos(a/2),2]\). Its degree is at most \(mD\), and (2)
has the loss \(mc_0\) on the whole interval. The crossing value at
a physical real angle has modulus one, and its derivative costs at
most a polynomial for fixed \(n\). Summing the \(N\) trace points
therefore preserves (17).

For complex external variables in the local polydisk, (11) gives
the corresponding estimate relative to
\(\sum_j\Re W(0,\mathbf u^{(j)})\), with loss at least
\(mc_0/2\). By (12) and (15), this is strictly below the
selected action. This justifies the removal of these original trace
points before any local expansion is used.

Set
\[
 f_N(t)=\prod_jF_N(t,\mathbf u^{(j)}),\quad
 g_N(t)=\sin t\,f_N(t)e^{inNt^2/(4\pi)},\quad
 \eta=(-1)^{N-1},\quad h=-\Im t_*(\mathbf U)>0.
\]
The exact midpoint trace identity is
\[
\begin{aligned}
 \mathcal D^{a_N}_{n,N}f_N
 ={}&-\frac{N^2C_{N,n}}{\pi i}
   \int_{-a_N-ih}^{a_N-ih}
        g_N(t)\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}\,dt\\
 &+\frac{\eta N^2C_{N,n}}\pi
   \int_{-h}^{h}
           \frac{g_N(a_N+iv)}{4\cosh^2(Nv/2)}\,dv .
\end{aligned}                                             \tag{18}
\]
It is the identity proved in
[the full internal trace argument](research_high_degree_short_internal_vertex.md),
Section 5. It holds for the present even polynomial of degree \(mD\).
The rational denominator retains every Fourier charge and its
multiplicity from the original normal derivatives.

By (12)--(14), the entire rectangle in (18) lies inside \(|t|<r\).
The product of the full block expansions (1) is uniform and
holomorphic on it:
\[
 f_N(t)=N^{m\alpha}\prod_j A(t,\mathbf u^{(j)})
        e^{N\sum_jW(t,\mathbf u^{(j)})}(1+O_m(N^{-1})).    \tag{19}
\]
There has been no application of \(R^n\) to the error in (19).
Instead (19) is inserted into the exact contour formula (18).

On the lower horizontal segment, (16) makes \(\Re\Phi\) strictly
concave as a function of its real coordinate. Its unique maximum
is at \(t_*(\mathbf U)\). The rational factor in (18) equals
\(e^{-iNt}(1+O(e^{-Nh}))\), so all its higher charges have a
strict exponential loss.

For the vertical integral, oddness of \(g_N\) folds the upper
half to the negative lower endpoint. Its absolute rate is bounded
at \(t=\pm a_N-iv\), \(0\le v\le h\), by \(\Re\Phi(t,\mathbf U)\):
\((4\cosh^2(Nv/2))^{-1}\le e^{-Nv}\) supplies exactly the
required charge loss. This rate is convex in \(v\), because its
second derivative is \(-\Re\Phi_{tt}>0\). At \(v=h\), horizontal
strict concavity gives a gap. At \(v=0\), (10) and evenness give
\[
 \Re\Phi(\pm a_N,\mathbf U)
 \le\sum_j\Re W(0,\mathbf u^{(j)})-\frac{m\kappa a^2}{4},
\]
strictly below \(\Re\mathcal S(\mathbf U)\) by (12),(15).
Convexity controls the whole vertical current. For fixed \(m,n\)
these gaps are uniform on a smaller closed boundary polydisk.

Gaussian expansion of the surviving lower horizontal integral proves
(6)--(7). Its factors in \(N\) are
\[
             N^{m\alpha}\,N^2\,N^{-1/2}
                         =N^{-3(mq-1)/2}.              \tag{20}
\]
The amplitude is nonzero: all block amplitudes are nonzero,
\(t_*\ne0\), \(|t_*|<r/4<1\), and the denominator in (7)
has positive real part before taking its square root. Uniform
holomorphic errors give the derivative assertions.

## 6. A whole-boundary bound, not only a local saddle

The global estimate requires an additional argument. Multiplying a
local expansion alone would not control boundary angles far from zero.

First the stationary action remains strictly concave in the small
real outside variables, with a constant independent of \(m,n\).
Let \(v\) be the vector of mixed derivatives
\(W_{t\mathbf u}\) from all \(m\) copies. The Schur complement is
\[
 \mathcal S_{\mathbf U\mathbf U}
 =\operatorname{diag}_j W_{\mathbf u\mathbf u}
       -\frac{vv^T}{\Phi_{tt}}.                          \tag{21}
\]
Equations (10),(14),(16) give
\[
 \left\|\frac{vv^T}{\Phi_{tt}}\right\|
 \le\frac{2B^2|t_*|^2}{\kappa}
 \le\frac{98B^2}{\kappa R_m^2}\le\beta/2.                \tag{22}
\]
Thus \(\Re(-\mathcal S'')\ge\beta I/2\) throughout the
chosen small polydisk. Separate evenness gives \(\mathcal S'(0)=0\).
For real \(|U_\ell|\le\rho\),
\[
                  \Re\mathcal S(\mathbf U)
                       \le M-\frac\beta4|\mathbf U|^2. \tag{23}
\]
The local expansion proves the required bound in this region.

For arbitrary real outside angles let
\(T(\mathbf U)=\sum_\ell(1-\cos U_\ell)\).
In (18) now use the fixed height \(h=-\Im t_*(0)\), and apply
the global bound (2), rather than the local expansion. For
\(t=x-iv\), \(|x|\le a_N\), \(0\le v\le h\), it gives the rate
\[
 mF_0-cT(\mathbf U)-mk_0x^2
                 +mC_1v^2+\frac{|n|}{2\pi}|x|v-v.       \tag{24}
\]
Here \(1-\cos x\ge2x^2/\pi^2\) for \(|x|\le\pi\).
The last term is supplied by the charge kernel; dropping it and
completing the square in \(x\) gives the upper bound
\[
 mF_0-cT(\mathbf U)
              +mC_1h^2+\frac{n^2h^2}{16\pi^2mk_0}
 \le mF_0-cT(\mathbf U)+\frac{K_0}{m}.                  \tag{25}
\]
The last inequality is uniform in \(n\): from (14),
\(h\le7D_m/(D_m^2+n^2)\), while
\(D_m^2n^2/(D_m^2+n^2)^2\le1/4\).
It applies to the entire lower horizontal segment and, after the
same odd folding, to the entire vertical current. Their prefactors
have only polynomial cost for fixed \(m,n\).

If some \(|U_\ell|\ge\rho\), then \(T(\mathbf U)\ge s_0\).
Equations (12),(15),(25) therefore imply
\[
     |\hbox{central trace}|
        \le C N^p e^{N\{M-cT(\mathbf U)/2\}}.             \tag{26}
\]
The original outer-angle contribution (17) has the same kind of
bound by (12),(15). Combining (23) and (26) proves a uniform
angular loss on the entire real boundary torus.

Finally extend it to a thin complex strip. In a small neighborhood
of zero, the holomorphic expansion and the strictly negative real
Hessian give a bound
\(M-c'|\mathbf X|^2+B'|\mathbf Y|^2\), by Taylor's theorem
and Young's inequality. Away from that neighborhood the real bound
has a fixed gap. Cover the compact real spectral region by finitely
many products of intervals, slightly enlarged while keeping a gap
in at least one coordinate. The polynomial Bernstein--Walsh bound,
using separate degrees at most \(D\), preserves half that gap in
a sufficiently thin fixed complex neighborhood. Reducing the
angular constant, and increasing the quadratic imaginary constant,
combines the two bounds into (8). No high-index or odd endpoint
term is omitted in this passage.

At zero, \(W_{tu_\ell}(t,\mathbf0)=0\) by separate evenness.
Thus (21) gives exactly (9), rather than just a sign estimate.
This completes the proof of Theorem 1.

## 7. Geometry and the volume theorem after the other fillings

The geometric input is proved in
[the marked gluing of the repeated zero blocks](research_amplified_zero_block_geometry.md).
The fixed zero block already has a positive strict Conway decomposition,
even when the former angle-edge coordinates had a fold. Glue these
actual cells at the common original circle. Their meridian increments
add, while the primitive longitude is \(V=2it\), traversed once.

Writing the central original power as \(n=\eta_v-2p_v\), its
carrier \(\eta_v\) is inserted once. Along the critical path in
Section 4 at complete outside boundary values,
\[
 U+p_vV=-2\pi i\lambda,\qquad
 \ell=-2\Im t_\lambda>0 .
\]
The fixed positive chart was included when choosing \(r\). Consequently
(14) gives the actual original primitive cone filling throughout
\(0\le\lambda\le1\). All other boundary cusps remain complete.
The complete anchor is \(2\pi mF_0\), and Schläfli's formula gives
the absolute volume of this partially filled parent as \(2\pi M\).
There is no additional exponential scalar.

**Corollary 2.** In an original marked circle-tree template, suppose a
connected selected region consists of \(m\ge m_0(\mathcal B)\)
copies of the above zero block attached to one original circle.
The center has exactly these \(m\) incidences: there is no additional
untouched edge incident to it outside the product (4).
Give that circle any fixed signed power \(n\), and give every
selected vertex in the copies power zero. Keep at least one original
circle outside the selected region. Then all independently sufficiently
long fixed signed powers at the remaining circles satisfy the original
Kashaev volume identity, provided the original component and framing
conditions give a knot:
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                       =\operatorname{Vol}(S^3\setminus K). \tag{27}
\]

To prove the corollary, insert the exact boundary polynomial (4) into
the untouched original source. Equations (6),(8),(9) are precisely
the local and global hypotheses of
[the complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md).
The original geometric gluing supplies the same primitive curves and
the absolute volume anchor. The remaining long cone deformations stay
in its positive chart. The long-filling proof then gives a nonzero
leading coefficient at the absolute final volume action.

For completeness, let \(B=mq\) be the number of edges leaving this
connected region, \(r\) the number of unfilled original vertices,
and \(e_0\) the number of untouched edges between them. The tree
identity gives \(e_0+B=r\). The pre-filling power of \(N\) is
\[
 -\frac32(B-1)-\frac32e_0=-\frac32(r-1).
\]
The \(r\) remaining original traces contribute \(N^{3r/2}\).
The closed source consequently has the usual \(N^{3/2}\) factor,
and all its framing scalars have modulus one. The copying operation
has introduced no hidden normalization factor.

This theorem handles a particular new class of adjacent short-filled
regions. The internal zero block may be any fixed degree-at-least-three
subtree, of arbitrary size; its neighboring central power need not be
long. It does not cover an arbitrary connected collection of nonzero
short powers, nor does it establish the full cofinite-assignment
statement. Its contribution to that problem is a proved composition
step with the full source, global boundary loss, and original geometry.

## 8. A finite check of the original composition

The script
[check_amplified_zero_block_composition.py](../experiments/check_amplified_zero_block_composition.py)
checks the gluing normalization by two independent finite representations.
The block is one trivalent zero-filled original vertex, with two
independent complex outside angles. One calculation contracts each block
in the full Newton quotient and applies the original signed crossing
matrix at the common circle. The other uses every physical derivative
trace node at each zero vertex and at the center, with the full product
rule and the central carrier inserted once.

Run
~~~sh
python3 experiments/check_amplified_zero_block_composition.py \
  --precision 100 \
  --output repro/results/research-amplified-zero-block-composition.json
~~~

The [saved record](../repro/results/research-amplified-zero-block-composition.json)
contains 32 comparisons: levels \(N=3,4,5,6\), multiplicities \(m=3,4\),
and central powers \(n=-2,0,1,3\). Every outside angle is retained and
the copies have distinct angle values. At 100 decimal digits the largest
relative difference is less than \(8.14\cdot10^{-100}\).
This checks the exact source, the parity and normal conventions, and the
once-only carrier. The tested multiplicities are not asserted to meet
(12); these finite identities do not test the asymptotic threshold or
replace its contour proof.


