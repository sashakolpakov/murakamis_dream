# Long fillings with a complex boundary phase

Research note, 2 November 2026. Frozen manuscripts are unchanged.

Eliminating a fixed short terminal filling generally produces a complex
function of its remaining boundary angle. There is no reason for the
imaginary part of that function to be quadratic. The long-filling
argument needs a negative real Hessian and a controlled complete finite
source; it does not need the source phase to be real.

The theorem below makes this distinction precise. It keeps the original
integer crossing powers in the exact trace and allows an arbitrary
separately even holomorphic local phase. Its proof uses the exact
complete-meridian contour from
[the rational trace note](research_exact_complete_trace_contour.md).
On a single translated contour, that formula sums all positive Fourier
charges before any estimate is made. In particular, the proof requires
neither a fractional replacement of a physical filling slope nor a
truncation of the Fourier series.

## 1. Hypotheses on the complete finite source

Fix $r\geq1$. For each integer $N\geq3$, let

\[
 B_N(\mathbf t)=b_N(-2\cos t_1,\ldots,-2\cos t_r)
\]

be a polynomial in the indicated variables. Thus $B_N$ is entire,
$2\pi$-periodic and separately even in its angles. Its separate degrees
may be any fixed multiples of $N-1$.

Assume the following two estimates describe this entire polynomial,
including every part of the original source.

First, on a fixed complex polydisk about $\mathbf0$,

\[
 B_N(\mathbf t)=\epsilon_N N^\alpha a(\mathbf t)
                   e^{NF(\mathbf t)}(1+E_N(\mathbf t)),
 \qquad |\epsilon_N|=1,
 \qquad \sup|E_N|\leq C/N.                                 \tag{1}
\]

The error is holomorphic, $\alpha\in\mathbb R$ is fixed, and $F,a$
are holomorphic functions independent of $N$. The phase $F$ is
separately even, $a(\mathbf0)\ne0$, and

\[
 F''(\mathbf0)=\operatorname{diag}(-a_j+ib_j),
 \qquad a_j>0,\quad b_j\in\mathbb R.                        \tag{2}
\]

Separate evenness already forces the off-diagonal Hessian entries to
vanish at zero. The notation $a_j$ in (2) denotes positive constants,
whereas $a(\mathbf t)$ is the amplitude in (1). No reality condition is
imposed on $F(\mathbf0)$ or on the higher Taylor coefficients of $F$.
Put $\Phi=\operatorname{Re}F(\mathbf0)$.

Second, there are positive constants $c,C_0,b,C$ and a fixed $A$ such
that

\[
 |B_N(\mathbf x+i\mathbf y)|
 \leq CN^A\exp N\left\{
   \Phi-c\sum_{j=1}^r(1-\cos x_j)+C_0\sum_{j=1}^r y_j^2
                         \right\},                        \tag{3}
\]

for every $|x_j|\leq\pi$ and $|y_j|\leq b$. The constants in
(1)–(3) belong to the fixed source family. They do not depend on the
long crossing powers chosen below.

The fixed degree bound is compatible with the original tree sources.
The contour argument itself uses only that the exact finite trace is
defined and that (1) and (3) hold on the stated sets; it never replaces
a higher-degree polynomial by its values at distinct roots.

## 2. The analytic theorem

Let $\mathcal D_{n,0,N}$ be the original complete-meridian crossing
trace in one angle. Its polynomial input may have arbitrary degree.
For signed integers $\mathbf n=(n_1,\ldots,n_r)$, define

\[
 T_{\mathbf n}(\mathbf t)
    =F(\mathbf t)+\frac{i}{4\pi}\sum_{j=1}^r n_jt_j^2
                                   -i\sum_{j=1}^r t_j,
 \qquad
 C_{N,n}=q^{n(N-1)^2/4},\quad q=e^{\pi i/N}.                \tag{4}
\]

**Theorem.** Under (1)–(3), there is a constant $n_0$ such that
for every fixed choice of signed integers $|n_j|\geq n_0$:

- $T_{\mathbf n}$ has a unique critical point $\mathbf t_*$ in a
  fixed small polydisk; each coordinate has negative imaginary part.
- The full original trace has the asymptotic

\[
 \begin{aligned}
 \left(\prod_{j=1}^r\mathcal D_{n_j,0,N}^{(j)}\right)B_N
   ={}&\epsilon_N\left(\prod_{j=1}^r C_{N,n_j}\right)
       N^{\alpha+3r/2}D(\mathbf n)
       e^{NT_{\mathbf n}(\mathbf t_*)}
       \bigl(1+O_{\mathbf n}(N^{-1})\bigr),\\
 D(\mathbf n)
   ={}&\left(-\frac1{\pi i}\right)^r(2\pi)^{r/2}
       \frac{a(\mathbf t_*)\prod_j\sin t_{*,j}}
            {\sqrt{\det[-T_{\mathbf n}''(\mathbf t_*)]}}
       \ne0.                                               \tag{5}
 \end{aligned}
\]

The square root is the Gaussian branch on complex symmetric matrices
with positive definite real part. The conclusion holds along all
integer levels $N$, including both parities and composite levels.
The threshold $n_0$ imposes no comparison between the magnitudes or
signs of different $n_j$.

The powers are fixed before $N\to\infty$. The theorem does not assert
a uniform error when the powers themselves grow with $N$.

## 3. The critical point and its real action

Separate evenness gives a holomorphic factorization

\[
 F_j(\mathbf t)=t_j Q_j(\mathbf t),\qquad
 Q_j(\mathbf0)=-a_j+ib_j.                                  \tag{6}
\]

Choose a small polydisk on which $a$ has no zeros and, for fixed
positive constants $a_*,M,L$,

\[
 \operatorname{Re}Q_j\leq-a_*/2<0,\qquad
 |Q_j|\leq M,\qquad \|DQ_j\|\leq L,
 \qquad -\operatorname{Re}F''\geq (a_*/2)I.                \tag{7}
\]

The last inequality is for real vectors and holds throughout the
complex polydisk. It follows by continuity from (2), after shrinking
the polydisk. As $F''$ is complex symmetric, it is also the statement
that the Hermitian part of $-F''$ is positive definite.

More generally, let $\boldsymbol\ell$ be a vector of nonnegative
real charges and consider

\[
 T_{\mathbf n,\boldsymbol\ell}
      =F+\frac{i}{4\pi}\sum_jn_jt_j^2-i\sum_j\ell_jt_j.
\]

Its critical equations are exactly

\[
 t_j=\frac{2\pi\ell_j/n_j}
                 {1-2\pi iQ_j(\mathbf t)/n_j}.             \tag{8}
\]

For $\boldsymbol\ell=\mathbf1$, the right side maps the chosen
polydisk into itself when every $|n_j|$ is sufficiently large. Its
row derivatives are $O(n_j^{-2})$, uniformly in the independent
signs and magnitudes. It is therefore a contraction. Every critical
point in the polydisk must satisfy (8), proving uniqueness there.
The same argument applies uniformly to $\ell_j\in[0,1]$.

Taking the imaginary part in (8) gives the exact formula

\[
 \boxed{\displaystyle
 \operatorname{Im}t_j=
 \frac{4\pi^2\ell_j\operatorname{Re}Q_j(\mathbf t)}
      {n_j^2|1-2\pi iQ_j(\mathbf t)/n_j|^2}.}               \tag{9}
\]

This formula is valid for complex $Q_j$. In particular, at unit
charge there are positive constants $c_1,C_1$, independent of the
chosen large powers, such that

\[
 \frac{c_1}{n_j^2}\leq y_j:=-\operatorname{Im}t_{*,j}
                         \leq\frac{C_1}{n_j^2},
 \qquad |t_{*,j}|\leq\frac{C_1}{|n_j|}.                    \tag{10}
\]

All coordinates are nonzero, so their sines are nonzero on the small
polydisk. The Hessian $-T_{\mathbf n}''$ has the same real part as
$-F''$ and is therefore accretive and invertible.

For completeness, scale all charges by a real parameter
$\lambda\in[0,1]$. Let $S(\lambda)$ be the stationary value.
Stationarity gives

\[
 \frac{d}{d\lambda}\operatorname{Re}S(\lambda)
       =\sum_j\operatorname{Im}t_j(\lambda).
\]

Equations (7)–(9) imply

\[
 0<\Phi-\operatorname{Re}T_{\mathbf n}(\mathbf t_*)
          \leq C_2\sum_jn_j^{-2},                          \tag{11}
\]

with a corresponding positive lower bound proportional to the same
sum. The stationary action therefore lies arbitrarily close to
$\Phi$ when all powers are independently large.

The all-charge comparison used in the earlier proof is also valid.
For a sufficiently small fixed $a_0>0$, (8) remains a contraction
when $0\leq\ell_j\leq a_0|n_j|$. If $S_{\boldsymbol\ell}$
denotes its stationary value, then

\[
 \partial_{\ell_j}\operatorname{Re}S_{\boldsymbol\ell}
      =\operatorname{Im}t_j,
 \qquad
 \operatorname{Re}S_{\boldsymbol\ell}
 \leq\operatorname{Re}S_{\mathbf1}
       -c_2\sum_j\frac{\ell_j^2-1}{n_j^2}
       \quad(\ell_j\geq1).                               \tag{12}
\]

These identities use the negative real part of $Q_j$, not a reality
assumption on $F$. The proof below does not need to find these other
critical points: the exact rational kernel estimates all their charges
on the single contour determined by $\mathbf t_*$.

## 4. The exact contour, with every normal retained

Put $\eta=(-1)^{N-1}$. In one coordinate, for an even entire
polynomial source $f$, define

\[
 g(t)=\sin t\,f(t)e^{inNt^2/(4\pi)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2}.
\]

The exact complete-meridian identity is

\[
 \begin{aligned}
 \mathcal D_{n,0,N}[f]
 ={}&-\frac{N^2C_{N,n}}{\pi i}
       \int_{-\pi-iy}^{\pi-iy}g(t)W_N(t)\,dt\\
 &+\frac{\eta N^2C_{N,n}}{\pi}
       \int_{-y}^{y}
         \frac{g(\pi+iv)}{4\cosh^2(Nv/2)}\,dv.             \tag{13}
 \end{aligned}
\]

It holds for every $y>0$. Here is the short derivation that explains
why it is the full trace. At the complete meridian,

\[
 \mathcal D_{n,0,N}[f]
      =\eta C_{N,n}\sum_{k=0}^{N-1}g'(\tau_k),
 \qquad \tau_k=\frac{2\pi}{N}\left(\frac{N-1}{2}-k\right).
\]

Apply the residue theorem on the rectangle $\pm\pi\pm iy$ to
$K_Ng'$, with $K_N=iNe^{iNt}/(e^{iNt}-\eta)$, and integrate
by parts. Reflect the upper side using that $K_N'$ is even and $g$
is odd. On the vertical sides,
$K_N'=-N^2/(4\cosh^2(Nv/2))$. These operations give (13).
The derivative sampling formula is the removable value of the
original trace at its colliding grid. In particular it includes the
first derivatives at every double root and the single odd-level
endpoint term. A full derivation is in
[the exact contour note](research_exact_complete_trace_contour.md).

Apply (13) in every coordinate with $y=y_j$ from (10). Separate
evenness of the exact source permits each reflection even when the
other coordinates are complex. The resulting finite expansion has
$2^r$ terms: one in which every coordinate is integrated horizontally,
and terms with at least one vertical endpoint current. There is no
infinite list of endpoint connectors.

In the all-horizontal term, write $t_j=x_j-iy_j$. Then

\[
 W_N(t_j)=e^{-iNt_j}\bigl(1+O_{\mathbf n}(e^{-Ny_j})\bigr),
                                                               \tag{14}
\]

uniformly for $|x_j|\leq\pi$. This is the exact sum of all positive
Fourier charges; its unit-charge coefficient is one. The original
integer $n_j$ remains in every chirp and every endpoint current.

## 5. Bounds outside the critical neighborhood

Choose a small fixed real box $Q=[-\delta,\delta]^r$ so that
$Q-i\mathbf y$ lies in the local polydisk for all sufficiently large
powers. Arrange also that $|\operatorname{Re}t_{*,j}|<\delta/2$.

For any coordinate on either a horizontal side or a vertical side of
(13), its imaginary part has absolute value at most $y_j$. Hence

\[
 \left|e^{in_jNt_j^2/(4\pi)}\right|
       \leq\exp\left(\frac{N|n_j|y_j}{2}\right),
 \qquad
 \sum_j |n_j|y_j=O\left(\sum_j|n_j|^{-1}\right).             \tag{15}
\]

All sine factors are bounded on the fixed strip. Horizontal rational
kernels are bounded by $4$ for sufficiently large $N$ at the fixed
powers; vertical kernels are at most $1/4$ in absolute value.

If a term has a vertical coordinate, its real angle is $\pi$ in
that coordinate. The source estimate (3) gives a loss at least $2c$.
The chirp cost in (15) and the $C_0\sum y_j^2$ cost tend to zero
as the powers become large. Thus all terms with a vertical current
have a bound

\[
 C_{\mathbf n}N^{A'}e^{N(\Phi-\gamma_1)}                   \tag{16}
\]

with a fixed $\gamma_1>0$, after increasing $n_0$. This estimates
all exact endpoint currents, including those that arise at odd levels.

In the all-horizontal term with $\mathbf x\notin Q$, at least
one angular loss is $c(1-\cos\delta)>0$. The same argument gives

\[
 C_{\mathbf n}N^{A'}e^{N(\Phi-\gamma_2)}.                  \tag{17}
\]

These estimates impose only a lower bound on each $|n_j|$. A single
very large power cannot make another coordinate's contour more costly:
its height is its own $O(n_j^{-2})$ quantity from (10).

By (11), increase $n_0$ once more so that the drop from $\Phi$ to
the unit-charge action is smaller than half both losses in (16) and
(17). The endpoint terms and the exterior horizontal region are then
exponentially below the selected action.

## 6. The local integral and its nonzero coefficient

On $Q-i\mathbf y$, insert the complete local expansion (1).
The phase, after extracting the first factor in (14), is exactly
$T_{\mathbf n}$. Along this translated real box,

\[
 \operatorname{Re}T_{\mathbf n}(\mathbf x-i\mathbf y)
 \leq\operatorname{Re}T_{\mathbf n}(\mathbf t_*)
          -c_3|\mathbf x-\operatorname{Re}\mathbf t_*|^2.  \tag{18}
\]

To see this, the real gradient vanishes at $\mathbf t_*$ and the
real Hessian along any horizontal line is $\operatorname{Re}F''$:
the physical quadratic chirp has purely imaginary Hessian. Apply
(7) on the straight segment from the critical point to the point
in question. This argument permits arbitrary complex higher Taylor
coefficients of $F$.

It follows from (18) that replacing every rational denominator in
(14) by one changes the integral by at most

\[
 C_{\mathbf n}N^{A'}
 e^{N\{\operatorname{Re}T_{\mathbf n}(\mathbf t_*)-
                         \min_j y_j\}}.                   \tag{19}
\]

Thus the complete family of higher Fourier charges is below the same
action. No separate estimate of their individual critical points or
possible signs is needed.

The remaining integral is

\[
 \epsilon_N N^\alpha
 \int_{Q-i\mathbf y}a(\mathbf t)\prod_j\sin t_j\,
             e^{NT_{\mathbf n}(\mathbf t)}(1+O(N^{-1}))
             \,d\mathbf t.                               \tag{20}
\]

Rescale about $\mathbf t_*$ by $N^{-1/2}$ in the real directions.
The bound (18) controls the complement of a shrinking neighborhood.
Taylor expansion inside it gives the complex Gaussian with matrix
$-T_{\mathbf n}''(\mathbf t_*)$. Its real part is positive definite,
so its integral is

\[
 (2\pi)^{r/2}\bigl(\det[-T_{\mathbf n}''(\mathbf t_*)]\bigr)^{-1/2}.
\]

The branch is the continuation from positive real symmetric matrices
inside the convex domain of accretive complex symmetric matrices.
The odd first correction integrates to zero; the holomorphic source
error and the remaining Taylor terms give a relative
$O_{\mathbf n}(N^{-1})$ error. Multiplying the exact horizontal
prefactor $(-N^2/(\pi i))^r\prod_jC_{N,n_j}$ yields (5).
Its coefficient is nonzero because the amplitude, the sines and the
Gaussian determinant are all nonzero. This proves the theorem.

## 7. Where a reality assumption could have entered

The earlier fixed-quadratic-phase lemma used a real phase $\Psi$.
Its relevant steps have the following requirements.

| Step | Property actually required |
|---|---|
| Pairing positive and negative Fourier modes | Separate evenness of the exact source; no conjugation symmetry. |
| Tail and endpoint estimates | The modulus bound (3) and the original real integer crossing powers. |
| Factoring $F_j=t_jQ_j$ | Separate evenness and holomorphy. |
| Locating the critical point below the real angles | The exact identity (9) and $\operatorname{Re}Q_j<0$. |
| Comparing stationary actions | Stationarity and the same negative real part, as in (12). |
| Gaussian integration | Accretivity of the complex Hessian, not a real Hessian. |
| Noncancellation of the leading term | A nonzero amplitude, nonzero sine factors and unit-charge coefficient one. |

The one local estimate that should not be justified by saying that
“the phase is real on the real box” is the shifted real-part bound.
For a complex phase it still follows directly from Taylor's theorem.
Writing $F''(0)=-A+iB$ with $A>0$ diagonal, the quadratic real part is

\[
 -\frac12\mathbf x^{\mathsf T}A\mathbf x
 +\frac12\mathbf y^{\mathsf T}A\mathbf y
 -\mathbf x^{\mathsf T}B\mathbf y.
\]

Young's inequality absorbs the mixed term into a portion of the
negative $\mathbf x$ quadratic form and a larger $\mathbf y$
quadratic form. Shrinking the polydisk absorbs the higher-order
terms. Consequently

\[
 \operatorname{Re}F(\mathbf x+i\mathbf y)
       \leq\Phi-c_4|\mathbf x|^2+C_4|\mathbf y|^2.
\]

No Schwarz reflection identity for $F$ is used. The direct rational
contour proof above is stronger in one respect: it does not need
local connecting faces at all. Its original horizontal contours
already pass through the chosen critical imaginary parts.

## 8. Conditional application to other verified terminal fillings

Consider a fixed original circle-tree knot template. Select a finite
set of its original terminal leaves and fix their physical crossing
powers. Suppose at least one vertex remains. Delete the selected
leaves from the tree only after taking their exact boundary
polynomials (3) of the general terminal-power note. Let $V_0,E_0$
be the remaining vertices and edges, and let $p(\ell)$ denote the
parent of a selected leaf.

For each selected leaf, assume that two independent tasks have been
completed.

First, its **whole finite boundary polynomial**, at the complete
meridian, has a proved holomorphic expansion and global bound

\[
 H_{\ell,N}(u)=\epsilon_{\ell,N}N^{\alpha_\ell}
       a_\ell(u)e^{NF_\ell(u)}(1+O(N^{-1})),
 \qquad |\epsilon_{\ell,N}|=1,
\]

\[
 |H_{\ell,N}(x+iy)|\leq CN^A
       e^{N\{\operatorname{Re}F_\ell(0)
                     -c_\ell(1-\cos x)+C_\ell y^2\}}.
                                                               \tag{21}
\]

Here $F_\ell$ is even and holomorphic, and $a_\ell(0)\ne0$.
These are assumptions about the complete finite polynomial, not just
its local critical equations.

Second, its geometry supplies a positive primitive cone path to the
actual short filling, a positive holomorphic continuation in the
parent boundary near zero, and a marked action $G_\ell$ such that

\[
 F_\ell(u)-G_\ell(u)\in i\mathbb R
             \quad\hbox{is constant in }u.                 \tag{22}
\]

The geometric statement must retain the original edge-block face
identifications, primitive meridian, all logarithmic periods and
complete main cusps. Its continued boundary geometry must agree with
the original faces attached to the remaining tree. It must supply the
absolute volume anchor at complete parent, rather than only a volume
differential.

The exact remaining source is then

\[
 B_N(\mathbf t)=\prod_{vw\in E_0}K_N(t_v,t_w)
                   \prod_\ell H_{\ell,N}(t_{p(\ell)}).      \tag{23}
\]

Using the full edge-kernel theorem, its local phase and power are

\[
 F(\mathbf t)=\sum_{vw\in E_0}\psi(t_v,t_w)
                   +\sum_\ell F_\ell(t_{p(\ell)}),
 \qquad
 \alpha=-\frac32|E_0|+\sum_\ell\alpha_\ell.                 \tag{24}
\]

Assume its aggregate real Hessian is strictly negative. This condition
is explicit:

\[
 \frac{\deg_{E_0}(v)}{2\pi}
      -\sum_{\ell:\,p(\ell)=v}\operatorname{Re}F_\ell''(0)>0
                         \qquad(v\in V_0).                 \tag{25}
\]

The product bounds in (21) and for the full edge kernels give (3),
provided every remaining vertex has a positive angular loss. In the
usual connected nontrivial tree situation this follows from an
incident remaining edge or a selected leaf. Thus the analytic theorem
applies to all independently sufficiently large remaining physical
crossing powers, with their original allowed parities.

To identify the real action with the actual volume, put

\[
 P(\mathbf t)=\sum_{vw\in E_0}\psi(t_v,t_w)
                   +\sum_\ell G_\ell(t_{p(\ell)}).
\]

By (22), $P$ and $F$ have the same derivatives and differ only by a
purely imaginary constant. The verified short-fill geometries assemble
at $\mathbf t=0$ to a complete partially filled exterior $Y'$.
Their absolute calibrations must give

\[
 \operatorname{Vol}(Y')=2\pi\operatorname{Re}P(0)
                            =2\pi\operatorname{Re}F(0).    \tag{26}
\]

The original marked period identities, after eliminating each short
leaf by stationarity, are

\[
 U_v=-2\pi P_v-i\eta_vt_v,\qquad V_v=2it_v,
 \qquad n_v=\eta_v-2p_v,
\]

\[
 U_v+p_vV_v=-2\pi\left(P_v+\frac{in_v}{2\pi}t_v\right).
                                                               \tag{27}
\]

Here $p_v$ is the original integer Dehn filling coefficient and
$\eta_v$ the fixed diagram carrier. These full-period identities and
their continued logarithmic lifts are part of the marked geometric
hypotheses; no principal logarithm is reset at $Y'$.

For cone parameter $\lambda\in[0,1]$, solve

\[
 P_v(\mathbf t)+\frac{in_v}{2\pi}t_v=i\lambda.              \tag{28}
\]

This is the critical-point contraction of Section 3, since $P_v=F_v$.
It remains uniformly close to zero, has $\operatorname{Im}t_v<0$
for $\lambda>0$, and satisfies

\[
 U_v+p_vV_v=-2\pi i\lambda,
 \qquad \text{core length}=-2\operatorname{Im}t_v>0.
\]

The original core-edge shapes remain positive near zero, while the
already short-filled blocks remain positive in their assumed
holomorphic neighborhoods. With the stipulated primitive periods,
the same local solid-torus completion used in the geometric paper
gives a positive cone metric of angle $2\pi\lambda$. At
$\lambda=1$ it is the complete hyperbolic metric on the actual filled
knot complement, for assignments whose fixed strand matching gives
a knot.

Finally define

\[
 \mathcal C(\lambda)=P(\mathbf t(\lambda))
       +\frac{i}{4\pi}\sum_vn_vt_v(\lambda)^2
                         -i\lambda\sum_vt_v(\lambda).
\]

Stationarity gives $d\operatorname{Re}\mathcal C/d\lambda
=\sum_v\operatorname{Im}t_v$. Schläfli's formula for the actual
positive cone metric gives the volume derivative
$2\pi\sum_v\operatorname{Im}t_v$. The initial equality (26)
therefore yields

\[
 \operatorname{Vol}(S^3\setminus K)
        =2\pi\operatorname{Re}T_{\mathbf n}(\mathbf t_*).
                                                               \tag{29}
\]

Combine (29), the exact finite source identity (23), its original
unit framing factors, and the analytic asymptotic (5). This proves

\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                          =\operatorname{Vol}(S^3\setminus K)
\]

under the explicitly stated packet and geometric hypotheses.
If each short packet has $\alpha_\ell=0$, as in the proved
two-crossing case, then $|E_0|=|V_0|-1$ and the nonzero leading
power remains $N^{3/2}$. In general it is
$N^{3/2+\sum_\ell\alpha_\ell}$, which does not change the
exponential volume limit.

This is a closure theorem for already verified short terminal
fillings. It does not prove the required packets for arbitrary short
powers, does not cover adjacent short-filled vertices without their
own joint packet theorem, and does not establish a finite-exception
statement for all filling assignments.
