# Recursive original-source estimates with a degree threshold independent of depth

A sufficiently large number of incoming pieces gives a small central
filling angle. To use that observation repeatedly, the boundary disk
and global estimates must survive each step. This note proves that
they do for the original one-boundary circle-tree sources. The
outgoing edge resets the boundary response; the accumulated volume
constant is kept separate.

The resulting threshold is independent of the depth and size of the
tree. Terminal powers must have magnitude at least two. Every
nonterminal power may be any fixed signed integer, including zero.
There is no long-filling requirement in the final theorem.

## 1. Exact rooted sources

For an original terminal vertex with fixed power \(p\), let
\[
 F_N(u)=H_{p,N}(u)=
             \phi_N^{(t)}\bigl(R^pK_N(t,u)\bigr),\qquad |p|\ge2.
                                                               \tag{1}
\]
Suppose \(m\) already constructed rooted pieces have full boundary
polynomials \(F_{\nu,N}(t)\). A new original vertex, with fixed signed
power \(n\), has one outgoing original edge. Its exact source is
\[
 F_{\mathrm{new},N}(u)=
 \phi_N^{(t)}\left[
    R^nK_N(t,u)\prod_{\nu=1}^mF_{\nu,N}(t)\right].          \tag{2}
\]
The final root has no outgoing edge, so its full closed source is
\[
 Z_N=\phi_N^{(t)}
                    \left[R^n\prod_{\nu=1}^mF_{\nu,N}(t)\right].
                                                               \tag{3}
\]
These are identities for the original finite trace and kernel. Each
original edge occurs once. Each crossing and its carrier occurs once.
The products are formed before taking the original Hermite quotient
trace, so values and first normals at repeated spectral roots are
retained. Every boundary polynomial in (1)--(2) has degree at most
\(D=N-1\) in \(-2\cos u\).

We prove an invariant set of estimates for these actual sources,
starting from the terminal theorem. There is no arbitrary replacement
of a block by a formal asymptotic.

## 2. The common invariant estimates

There are fixed positive constants
\[
                  R,\ H,\ a_0,\ c,\ C,\ b
\]
and an integer \(M_*\) with the following property. Every actual
source produced by (1)--(2), using at least \(M_*\) children at
each application of (2), has

\[
 F_N(u)=\epsilon_N A(u)e^{NW(u)}(1+O_F(N^{-1})),\qquad
                         |\epsilon_N|=1,                 \tag{4}
\]
uniformly and holomorphically on a neighborhood of the closed disk
\(|u|\le2R\). The functions \(W,A\) are separately even in their
one variable; \(A\) has no zero on that disk. The normalized action
satisfies
\[
 w(u)=W(u)-W(0),\qquad
 |w(u)|\le H,\qquad
                    \Re[-W''(u)]\ge a_0
                       \quad(|u|\le2R).                 \tag{5}
\]
The full polynomial also satisfies
\[
 |F_N(x+iy)|
 \le C_FN^{d_F}
    \exp N\{\Re W(0)-c(1-\cos x)+Cy^2\},
 \qquad |x|\le\pi,\quad |y|\le b.                         \tag{6}
\]
Only \(C_F,d_F\), the error in (4), and its starting level depend
on the fixed piece. In particular no lower bound for \(|A(0)|\)
uniform over all pieces is asserted.

The fixed disk in (4) does not shrink under (2). The constants in
(5)--(6) do not deteriorate with the number of vertices. The original
positive marked geometry also exists on this disk, as proved in
[the recursive geometric construction](research_recursive_marked_block_geometry.md).

## 3. Choosing the constants before the recursion

Here is a noncircular construction of the constants and a sufficient
integer threshold.

Start with the common terminal estimates for all \(|p|\ge2\) proved
in [the uniform terminal-family note](research_uniform_terminal_family_and_star_fillings.md).
They give a positive common source and geometry radius, uniform phase
derivative bounds, strictly negative real curvature, and common global
constants \(c_T,C_T,b_T\).

The full bare edge has a common global estimate
\[
 |K_N(x+iy,v+iw)|
 \le C_eN^{d_e}\exp N\{\psi(0,0)
    -c_e(1-\cos x)-c_e(1-\cos v)+C_e'(y^2+w^2)\}.        \tag{7}
\]
The whole-kernel passage, including omitted indices, is proved in
Section 5 of the uniform terminal-family note. Its local full
expansion has factor \(N^{-3/2}a_e(t,u)e^{N\psi(t,u)}\).
Choose \(R>0\) so small that:

- the terminal packets and their positive geometry hold on a
  neighborhood of \(|u|\le2R\);
- the full edge packet, nonzero amplitude and positive geometry hold
  on a neighborhood of \(|t|,|u|\le2R\);
- \(2R\) is smaller than the imaginary strip width in (7);
- on that edge bidisk,
  \[
               \Re[-\psi''(t,u)]\ge a_e^* I
  \]
  for a fixed \(a_e^*>0\), and the terminal actions satisfy
  \(\Re[-W_p''(u)]\ge a_T>0\);
- the removable normalized edge slope
  \(-\psi_t(t,u)/((2\pi)^{-1}t)\) differs from \(1\) by at most
  \(1/100\) on that bidisk.

These choices are possible by the uniform terminal result and the
complete edge Hessian
\(-\psi''(0,0)=(2\pi)^{-1}I\).
Set \(a_0=\min(a_T,a_e^*)\). Define
\[
 L_e=\sup_{|t|,|u|\le2R}\left|\frac{\psi_u(t,u)}u\right|,
 \qquad
 H\ge\max\left\{
   \sup_{|p|\ge2,\,|u|\le2R}|W_p(u)-W_p(0)|,\ 2L_eR^2
                         \right\}.                      \tag{8}
\]
The quotient at \(u=0\) is removable by evenness; all these constants
are finite. Increase \(H\) if necessary.

The common real angular coefficient that the output will have is
\[
              \gamma=\min(c_e/2,a_e^*),\qquad
              \Delta=\gamma(1-\cos(R/4))>0.              \tag{9}
\]
Choose once and for all
\[
 c\le\min(c_T,c_e,\Delta/8,a_0/4).
\]
Let \(L_2=2H/R^2\), and choose
\[
 C\ge\max\{C_T,C_e',L_2^2/a_0+L_2/2\}.                  \tag{10}
\]
For the fixed spectral interval
\(I=[-2\cos(R/4),2]\), its Green function \(g_I\) is continuous
and zero on \(I\). Hence there is \(b_{\rm out}>0\) such that
\[
 g_I(-2\cos(x+iy))\le\Delta/2
       \quad(R/2\le|x|\le\pi,\ |y|\le b_{\rm out}).
\]
Set
\[
 b\le\min(b_T,\ b_{\rm edge},\ b_{\rm out},\ R/2).        \tag{11}
\]
All global invariant constants have now been chosen, before the
threshold \(M_*\).

To choose a central cutoff, note that every even phase satisfying (5)
has Taylor coefficient bounds
\[
 [u^{2k}]w(u)\ \le\ H/(2R)^{2k}
\]
in modulus. Write
\(-W''(0)=a-ib_W\), so \(a\ge a_0\) and
\(|b_W|\le H/(2R^2)\). The normalized slope
\[
 Q_W(t)=-\frac{W'(t)-ib_Wt}{at}
\]
therefore satisfies \(Q_W(0)=1\), uniformly
\[
 |Q_W(t)-1|\le1/100,\qquad |Q_W'(t)|\le L              \tag{12}
\]
on some fixed disk \(|t|\le r<R/2\). For example its first bound
follows by choosing \(r\) so that
\[
 \frac{H}{2a_0R^2}
 \left\{\left(1-\frac{r^2}{4R^2}\right)^{-2}-1\right\}
                                                    \le1/100 .
\]
The derivative bound follows by differentiating the same convergent
coefficient majorant. Enlarge \(L\) to include the derivative bound
for the edge slope on \(|t|\le r,\ |u|\le2R\). Its value bound
was already required in the initial choice of \(R\).
All constants have therefore been fixed in the stated order.
No recursion depth enters.

Put
\[
\begin{gathered}
 a_{\rm cut}=r/2,\quad c_0=c(1-\cos(a_{\rm cut}/2)),\quad
 d_{\min}=2\pi a_0,\quad b_{\max}=H/(2R^2),\quad k_0=2c/\pi^2,\\
 L_0=7/(2d_{\min}),\qquad
 \Gamma=4C_e'R^2+
        \sup_{|u|\le2R}|\psi(0,u)-\psi(0,0)|,\\
 K_0=\frac{49}{d_{\min}^2}
           \left(C+C_e'+\frac{b_{\max}^2}{2k_0}\right)
                         +\frac{49}{32\pi^2k_0}.
\end{gathered}
\]
A sufficient \(M_*\) is any integer at least three such that all
\(m\ge M_*\) satisfy
\[
\begin{gathered}
 d_{\min}m\ge\max(28/r,14/b),\qquad
 \frac{2\pi L}{(99/100)^2d_{\min}m}<1/2,\\
 \Gamma\le mc_0/4,\qquad L_0/m\le mc_0/4,\qquad
 L_0/m\le ma_0a_{\rm cut}^2/4,\\
 (K_0+L_0)/m\le
                     \frac{c_e}{2}(1-\cos(R/2)).
                                                               \tag{13}
\end{gathered}
\]
These are finitely many inequalities between fixed constants.
They are eventually satisfied. They provide one universal sufficient
threshold for the original source conventions; no numerical value is
claimed here.

## 4. The small central critical point on the unchanged output disk

Suppose the \(m\) actual child sources satisfy (4)--(6). Write
\[
 -W_\nu''(0)=a_\nu-ib_\nu,\quad
 A=\sum_\nu a_\nu+\frac1{2\pi},\quad B=\sum_\nu b_\nu,\quad
 D=2\pi A,\quad \widetilde n=n+2\pi B .
\]
For the total phase
\[
 \Phi_\lambda(t,u)=
    \sum_\nu W_\nu(t)+\psi(t,u)
                    +\frac{in}{4\pi}t^2-i\lambda t,
\]
the normalized slope is the \(a_\nu\)-weighted average of the child
slopes in (12) and the edge slope, with total weight \(A\).
Call it \(\overline Q(t,u)\). The exact critical equation is
\[
 t=\frac{-2\pi i\lambda}{D\overline Q(t,u)-i\widetilde n}.
                                                               \tag{14}
\]
The original power \(n\) has not been replaced in the finite source:
\(\widetilde n\) is only the total imaginary quadratic coefficient.

Equations (12)--(13) give a contraction uniformly for
\(|u|\le2R\) and \(0\le\lambda\le1\). Its unique critical branch is
holomorphic in \(u\), and
\[
 |t_\lambda(u)|\le
       \frac{7\lambda}{(D^2+\widetilde n^2)^{1/2}}
                              \le r/4,
 \qquad
 0<-\Im t_\lambda(u)\le
       \frac{7\lambda D}{D^2+\widetilde n^2}\le b/2.       \tag{15}
\]
The sign follows from \(\Re\overline Q>0\), also for complex \(u\).
The selected value \(W_{\rm new}(u)=\Phi_1(t_*(u),u)\) obeys
\[
 0<
 \sum_\nu\Re W_\nu(0)+\Re\psi(0,u)-\Re W_{\rm new}(u)
                                                    \le L_0/m. \tag{16}
\]
The output disk is \(|u|\le2R\), exactly the input source disk.
Children are only evaluated in the much smaller central disk.

## 5. Exact trace asymptotics and its currents

The local expansion of the exact integrand in (2) is
\[
 \left(\prod_\nu\epsilon_{\nu,N}\right)N^{-3/2}
 a_e(t,u)\prod_\nu A_\nu(t)
 e^{N\{\psi(t,u)+\sum_\nu W_\nu(t)\}}
                         (1+O_F(N^{-1})).
\]
It is uniform on the fixed central rectangle and the unchanged
closed output disk. Its error may depend on all the fixed child
pieces; it is never passed through an uncontrolled crossing norm.

Use the same exact midpoint trace identity as in
[the repeated-block proof](research_amplified_zero_block_source.md),
Section 5, with the original chirp \(n\), midpoint
\(a_N=a_{\rm cut}+O(N^{-1})\) chosen with
\(a_N\ge a_{\rm cut}\), and
\(h=-\Im t_*(u)>0\). All positive charges and the complete vertical
endpoint current remain in that identity.

For the discarded outer physical trace points, the child estimates
(6) and polynomial Markov inequality give the rate
\(\sum_\nu\Re W_\nu(0)-mc_0\), including first normals.
The outgoing edge at complex \(|u|\le2R\) costs at most
\(\psi(0,0)+4C_e'R^2\), by (7). Relative to the zero-charge
baseline at that \(u\), this is at most
\[
 \sum_\nu\Re W_\nu(0)+\Re\psi(0,u)-mc_0+\Gamma.
\]
Equations (13),(16) put it strictly below the selected action,
uniformly on the same output disk. The outside-variable cost is a
single \(\Gamma\); it is not multiplied by \(m\).

On the lower horizontal contour,
\[
 \Re\Phi_{tt}=\sum_\nu\Re W_\nu''+\Re\psi_{tt}
                                      \le-ma_0-a_e^*<0 .
\]
Thus its critical point is the unique real-action maximum. Higher
charges lose the fixed positive depth for each fixed source.
Oddness folds the vertical current to the two lower endpoints.
Its rate is convex in the depth. The real endpoint loses at least
\(ma_0a_{\rm cut}^2/2\), and the lower endpoint has the horizontal
strict gap. Conditions (13) control the whole current. These arguments
hold uniformly on the closed output disk.

Gaussian expansion proves (4) for the new actual polynomial, with
\[
\begin{split}
 \epsilon_{\rm new,N}
    &=C_{N,n}\prod_\nu\epsilon_{\nu,N},\\
 A_{\rm new}(u)
    &=i\sqrt{\frac2\pi}\,
      \frac{\sin t_*(u)\,a_e(t_*(u),u)\prod_\nu A_\nu(t_*(u))}
      {\sqrt{-\sum_\nu W_\nu''(t_*(u))
                    -\psi_{tt}(t_*(u),u)-in/(2\pi)}} .    \tag{17}
\end{split}
\]
Every factor is nonzero on the unchanged disk. The square root is
the Gaussian branch. The powers \(N^{-3/2}N^2N^{-1/2}\)
cancel, so no new power of \(N\) appears in a one-boundary piece.

## 6. The outgoing edge resets the phase

Stationarity gives the exact envelope identity
\[
                         W_{\rm new}'(u)=\psi_u(t_*(u),u).
                                                               \tag{18}
\]
Integrating it on the segment from zero to \(u\), and using (8), gives
\[
                   |W_{\rm new}(u)-W_{\rm new}(0)|
                                      \le L_e|u|^2/2\le H .
\]
This proves the normalized phase bound without summing errors over
descendants.

The curvature bound is exact as well. At the critical point form
\[
 \mathcal H=-\begin{pmatrix}
 \sum_\nu W_\nu''+\psi_{tt}+in/(2\pi)&\psi_{tu}\\
 \psi_{ut}&\psi_{uu}
 \end{pmatrix}.
\]
Its Hermitian part is at least \(a_e^*I\), since the children add
nonnegative real central mass and the signed chirp is purely imaginary.
The outgoing negative Hessian is its Schur complement. Put
\(v=(-\mathcal H_{11}^{-1}\mathcal H_{12},1)^T\); then
\(\mathcal H v=(0,-W_{\rm new}'')^T\). Hence
\[
 \Re[-W_{\rm new}''(u)]
       =\Re(v^*\mathcal H v)\ge a_e^*\|v\|^2
                                      \ge a_e^*\ge a_0 . \tag{19}
\]
This holds on the same complex output disk. Thus (5) closes.

There is also a useful stronger comparison. Evenness in \(t\) and \(u\)
gives
\(\psi_u(t,u)-\psi_u(0,u)=t^2u\,L(t,u)\), with \(L\) uniformly
bounded on the fixed bidisk. By (15),(18),
\[
 \left|W_{\rm new}(u)-W_{\rm new}(0)
                 -\psi(0,u)+\psi(0,0)\right|
                                  \le C_2|u|^2/m^2.     \tag{20}
\]
Cauchy's formula yields corresponding derivative bounds on smaller
fixed disks. The volume constant has a loss of order \(1/m\),
but the normalized boundary response differs from the single-edge
response by order \(1/m^2\), independently of the number of descendants.

## 7. Resetting the whole-period bound and complex strip

For a real outside angle \(u\), the global bounds of the children and
the outgoing edge insert the loss
\(c_e(1-\cos u)\) into every central contour. Complete the square
in its real central coordinate. As in the finite-block proof, the
original \(n\), not merely \(\widetilde n\), obeys
\[
 n^2\le2\widetilde n^2+8\pi^2m^2b_{\max}^2.
\]
The whole central contour is consequently bounded by a polynomial
times
\[
 \exp N\left\{\sum_\nu\Re W_\nu(0)+\psi(0,0)
                 -c_e(1-\cos u)+K_0/m\right\}.           \tag{21}
\]
This estimate includes the lower horizontal integral, all its charges,
and the folded vertical current. The outer physical trace points
retain their larger loss \(mc_0\).

For \(|u|\ge R/2\), conditions (13),(16) turn (21) into a bound
with exponent
\(\Re W_{\rm new}(0)-c_e(1-\cos u)/2\).
For \(|u|\le R\), (19), evenness and the local expansion give the
stronger real rate
\(\Re W_{\rm new}(0)-a_e^*u^2/2\).
Together these yield a full real-period bound with coefficient
\(\gamma\) in (9), independent of the child pieces.

The complex strip is reset from this bound, rather than inherited
with a smaller coefficient. On the real spectral interval \(I\)
chosen in Section 3 the source loses \(\Delta\).
Its separate degree is at most \(N-1\), so Bernstein--Walsh and
(11) imply a loss at least \(\Delta/2\) whenever
\(R/2\le|x|\le\pi,\ |y|\le b\). Since
\(2c\le\Delta/4\), this is stronger than the required far-angle
part of (6).

For \(|x|\le R/2,\ |y|\le b\le R/2\), Cauchy's estimate from (5)
bounds \(|W_{\rm new}''|\) by \(L_2\) along the relevant paths.
Taylor's theorem and Young's inequality give
\[
 \Re W_{\rm new}(x+iy)
 \le\Re W_{\rm new}(0)-\frac{a_0x^2}{4}
                         +(L_2^2/a_0+L_2/2)y^2 .
\]
Equations (9)--(11) make this at least as strong as (6).
The amplitude and source error contribute only source-dependent
prefactors and starting levels. Thus all the invariant constants,
including the strip width, have been restored. This closes the
induction on arbitrary finite depth.

## 8. The final root and the knot-volume theorem

At the final root omit the outgoing kernel as in (3).
For at least \(M_*\) children the same contraction and whole-trace
argument apply, with no output variable or outside-variable cost.
Its nonzero asymptotic has factor \(N^{3/2}\):
\[
 Z_N=\Omega_N N^{3/2}D_0e^{NS}(1+O(N^{-1})),
                      \qquad |\Omega_N|=1,\quad D_0\ne0. \tag{22}
\]
The geometry proved in the companion note glues the original child
annuli, retains every previously filled primitive period, and inserts
the new carrier once. Bounds (15) keep each new charge path inside the
common positive charts. Formula (19) also supplies its nondegeneracy.
Schläfli calibrates the action from the sum of the complete child
volumes at every step. Thus the final action is the absolute
hyperbolic volume action. No auxiliary cusp remains after (3).

**Theorem.** There is a universal finite integer \(M_*\) for the original
circle-tree construction with the following property. Root a finite
tree at a nonterminal vertex. Suppose every terminal power has
magnitude at least two, every nonroot nonterminal vertex has at least
\(M_*\) children, and the root has at least \(M_*\) children.
Every nonterminal crossing power may be any fixed signed integer.
For every original carrier and component pattern yielding a knot,
the knot is hyperbolic and
\[
 \boxed{\displaystyle
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
                         =\operatorname{Vol}(S^3\setminus K).}
                                                               \tag{23}
\]
All levels, including both parities, are included.

In particular the theorem applies to every such unrooted tree whose
nonterminal degrees are all at least \(M_*+1\), regardless of its
number of vertices. The constant is independent of the depth, total
size, signs, and fixed magnitudes of its crossing powers.
The error constants and starting level may depend on the whole fixed
assignment; this is not a simultaneous limit in the powers and \(N\).

The theorem proves a general closure step for many adjacent nonzero
fillings. It still requires large valence and excludes terminal
powers \(0,\pm1\). It therefore does not establish the full
cofinite-assignment statement for an arbitrary fixed template.

## 9. Finite checks of the recursive normalization

The script
[check_recursive_original_tree_contraction.py](../experiments/check_recursive_original_tree_contraction.py)
compares two complete finite calculations: recursion with the original
Newton multiplication and crossing matrices, and recursion using every
physical derivative-trace node. It retains the value and first derivative
at a free complex boundary as well as the final closed-root trace.

~~~sh
python3 experiments/check_recursive_original_tree_contraction.py \
  --precision 120 \
  --output repro/results/research-recursive-original-tree-contraction.json
~~~

The [saved record](../repro/results/research-recursive-original-tree-contraction.json)
checks four irregular trees through depth five at \(N=2,\ldots,7\).
For each of the 24 level/tree pairs it compares three outside boundary
values and their derivatives, and the closed root. Every comparison
passed at 120 decimal digits; the largest relative discrepancy is below
\(1.71\cdot10^{-117}\).

These small trees deliberately test exact recursive composition and
signed powers, including internal \(0,\pm1\). They are not asserted to
satisfy the branching threshold. The finite checks do not establish
that threshold or replace the uniform analytic induction above.


