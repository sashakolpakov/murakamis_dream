# Two remaining residue indices for the type-four terminal source

Research deduction and conditional current criterion, 5 November 2026.
The complete ordinary endpoint coefficient can be retained exactly
inside the type-four terminal source. Its proved complex packet then
removes the Newton index from the remaining contour problem. This
leaves eight flattened constant-mode comparisons and twelve alias
families on an explicit asymmetric rectangle. Their signs are not
proved here. The exterior physical support is a separate obligation.

## 1. Exact interpolation after the complete inner sum

Use the notation and original branches of
[the joint type-four source](research_mixed_terminal_four_joint_source.md).
The already specified complete endpoint coefficient is
\[
 \mathcal C_N(e,w)=\sum_{l=0}^{N-1}
   \frac{e^{i\pi e l}e_l(w)}{S_lG_N(Ne-l)}.
 \tag{1}
\]
At \(e=j/N\), terms with \(l>j\) vanish exactly, and
\(\mathcal H_N(w,r^{-j})/P_j=\Delta_N(e)^{-1}\mathcal C_N(e,w)\).
This equality is for the whole ordinary polynomial, including all
jets and both level parities. Thus the exact reversed-cap formula is
\[
 \mathcal V_{1,N}(w,X)=
 \sum_{i+j<N}\frac{X^{-i}p_i(X)P_{i+j}}{P_i^3P_j}
                  \Delta_N(j/N)^{-1}\mathcal C_N(j/N,w).
 \tag{2}
\]
In particular no partial Newton sum is estimated by a bound for a
coherently summed cap.

For complex \(a,e,t\), define the exact retained interpolant
\[
 \widehat{\mathcal J}_N(a;e,t,w)=
 e^{2\pi iNat}
 \frac{\mathfrak P_N(a+t)\mathfrak P_N(e+t)}
      {\mathfrak P_N(a)\mathfrak P_N(t)^3\mathfrak P_N(e)}
                  \Delta_N(e)^{-1}\mathcal C_N(e,w).
 \tag{3}
\]
Here \(\mathfrak P_N\), \(\Delta_N\), and \(G_N\)
are precisely the prescribed interpolants in the joint-source note.
The factorial difference equation proves that (3) equals the summand
in (2) at every retained lattice pair. The full function (1), rather
than its asymptotic approximation, defines (3) on every contour.
Its off-grid rows with \(l>j\) are therefore retained whenever
the private coordinate leaves its physical grid.

Take
\[
\begin{split}
 a&\in[.22,.45]+i[-.12,.12],\qquad
 t\in[.15,.50]+i[-.12,.12],\\
 e&\in E_{\rm cap}=[.27,.49]+i[-.055,.04].
\end{split}
 \tag{4}
\]
The [complete endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md)
proves, on a fixed neighborhood of the last rectangle and complete
ordinary color,
\[
 \mathcal C_N(e,w)=N^{-3/2}A_C(e,w)e^{NS(e,w)}(1+O(N^{-1})),
 \qquad A_C\ne0.
 \tag{5}
\]
All fixed joint derivatives are uniform on smaller neighborhoods.
Every marked factorial in (3) is regular on (4), since
\(\Re(a+t)\in[.37,.95]\) and
\(\Re(e+t)\in[.42,.99]\).
The retained real rectangle lies strictly inside \(i+j<N\).

Let \(u_c(e)\) be the original critical branch of (1). At complete
color the phase of (3) is exactly
\[
 \widehat{\mathcal F}_1(a;e,t)
       =\mathcal F_1(a;e,t,u_c(e)),
 \tag{6}
\]
with no additional constant or logarithmic lift. This follows by
substituting \(S(e)=B(e,u_c(e))+i\pi e u_c(e)\) into the
unsimplified marked phase in the joint-source note. Its uniform symbol is
\[
 \widehat{\mathcal J}_N
 =N^{-3}\widehat A_1(a,e,t,w)
                  e^{N\widehat{\mathcal F}_1(a;e,t,w)}(1+O(N^{-1})),
 \tag{7}
\]
where, at complete color,
\[
 \widehat A_1=
 e^{i\pi(e+t)/2}A_C(e,-2)
 \frac{\sqrt{2\sin\pi(a+t)}\sqrt{2\sin\pi(e+t)}}
 {(2\sin\pi a)^{1/2}(2\sin\pi t)^{3/2}(2\sin\pi e)^{1/2}}.
 \tag{8}
\]
It is nonzero with the original square-root branches. The powers
are \(N^{-3/2}\) from the marked factorial quotient and
\(N^{-3/2}\) from (5).

## 2. Schur curvature on the asymmetric rectangle

**Lemma 1.** On the full product (4),
\[
                -\Re\widehat{\mathcal F}_1''\succ
                                      \frac\pi{100}I_3.
 \tag{9}
\]
The variables are \((a,t,e)\).

The endpoint theorem certifies on all of \(E_{\rm cap}\) that
\(.17<\Re u_c<.28\), \(.001<\Im u_c<.1\), and
\(0<\Re(e-u_c)<1/2\). The quadratic-form proof of the broader
joint Hessian bound therefore applies pointwise at \(u=u_c(e)\).
Here is the only extension needed beyond its independent box
\(u\le.269\). That bound used the upper endpoint solely to
ensure \(C(e-u)>0\), where \(C(z)=\Re\cot\pi z\).
The endpoint theorem supplies this sign directly. All other rows
depend only on \(a,t,e\), while
\(C(u_c)>7/12\) follows from the same scalar lower function
and \(.17<\Re u_c<.28<.30\), \(|\Im u_c|<.12\).
Thus the positive \(u\)-coefficient remains greater than
\(7/4\). Summed imaginary parts stay within the bounds used
in that proof. Its full four-variable negative Hessian is therefore
still greater than \((\pi/100)I_4\) at these points.

For a vector \(v\) in the three retained variables, append
\(u_c'(e)v_e\) to form \(\widetilde v\). Differentiating
the original equation \(\mathcal F_{1,u}=0\) makes the
last component of \(\mathcal F_1''\widetilde v\) zero.
The accretive Schur identity consequently gives
\[
 \Re\{v^*(-\widehat{\mathcal F}_1'')v\}
 =\Re\{\widetilde v^*(-\mathcal F_1'')\widetilde v\}
 >\frac\pi{100}\|\widetilde v\|^2
 \ge\frac\pi{100}\|v\|^2.
 \tag{10}
\]
This proves (9). No independent product extending across
\(\Re(e-u)=0\) is asserted.

At an actual external reference \(a_*=A+iH\), keep its
original \((e_*,t_*)=(E+ih_e,T+ih_t)\). The phase in (6)
has value \(\mathcal P_1(a_*)\), zero internal derivatives,
and external derivative \(\mathcal P_1'(a_*)\). Put
\[
 B_1(a_*;y)=\Re\mathcal P_1(a_*)+
       \Re\mathcal P_1'(a_*)(y-A)-\kappa(y-A)^2,
       \qquad\kappa=1/2500000.
 \tag{11}
\]
The horizontal-horizontal current at heights \((h_t,h_e)\)
is bounded by this plane, with the stronger quadratic loss
\(\pi/200\) in all three displacements. At any internal cut,
the index displacement has magnitude at least \(.063\), using
the actual private and attached rectangles. Its limiting boundary
therefore has gap greater than \(1/20000\) below (11):
\((\pi/200)(.063)^2>1/20000\).

## 3. The sufficient outer-current comparisons

The first group consists of eight zero-penalty comparisons:

* Two flattened \(t\)-faces: \(t=.15,.50\) real, and
  \(e=x_e+ih_e\) with \(x_e\in[.27,.49]\).
* Two flattened \(e\)-faces: \(e=.27,.49\) real, and
  \(t=x_t+ih_t\) with \(x_t\in[.15,.50]\).
* Four real-real corners.

The external target is always \(a=y+iH\), \(y\in[.22,.45]\).
Require their phases \(\Re\widehat{\mathcal F}_1\) to be
at most \(B_1-\delta_0\) for some uniform \(\delta_0>0\).
These are hypotheses, not consequences of Lemma 1.

For aliases, all real targets \((y,x_t,x_e)\) are free in their
entire intervals. The twelve required families are:

| Families | Internal heights \((\Im t,\Im e)\) | Penalty |
|---|---|---|
| Four \(t\)-single aliases | \((\pm.12,\sigma h_e)\), \(\sigma=0,1\) | \(.24\pi\) |
| Four \(e\)-single aliases | \((\sigma h_t,-.055)\) or \((\sigma h_t,.04)\), \(\sigma=0,1\) | \(.11\pi\) or \(.08\pi\), respectively |
| Four double aliases | \((\pm.12,-.055)\) or \((\pm.12,.04)\) | \(.35\pi\) or \(.32\pi\), respectively |

Require each tested phase minus its penalty to be at most
\(B_1-\delta_A\), with \(\delta_A>0\) uniform.
Only an aliased coordinate pays a residue penalty. Retaining an
actual height in the other coordinate does not add one.

These hypotheses cover every current. For each index choose inward
half-grid real cuts. With
\(K_N(z)=(1-e^{-2\pi iNz})^{-1}\), the exact summation
functional is \(N(I+A)\): the lower rectangle carries
\(K_N-1\), and the upper rectangle carries \(K_N\).
Its residue coefficient is positive \(N\). On a vertical
half-grid side,
\[
 K_N(c_N+ih)=\frac1{1+e^{2\pi Nh}},
 \tag{12}
\]
so the relevant kernel costs \(2\pi|h|\), including the
bounded value \(1/2\) at height zero. This formula works with
the unequal positive and negative heights in (4).

Deform each unaliased interval into its horizontal segment at the
actual height and its two vertical joins. There are nine constant-mode
currents, of which eight contain a join, and seventy-two alias
currents: \(18+18+36\). Convexity in each height reduces an
ordinary join to its endpoints at zero and the actual height.
On each sign half of an alias side the subtracted kernel penalty is
linear, so the same convexity reduces it to zero and that side's
outer height. The resulting vertices are exactly the twelve alias
families, the eight flattened comparisons, or restrictions of the
already controlled horizontal-horizontal boundary. This is the
[double-cycle argument](research_mixed_terminal_three_alias_reduction.md#3-completeness-after-deforming-the-unaliased-coordinate)
with the two unequal \(e\)-heights kept literally.

At the actual half-grid cuts this is an exact identity. Their
\(O(N^{-1})\) displacements change the rates by
\(O(N^{-1})\), since all source factors stay regular on a
fixed compact neighborhood. The small ordinary-color perturbation,
polynomial prefactors and finite number of currents are paid from
one common strict gap.

**Proposition 2 (conditional rectangular packet).** If the eight
flattened comparisons and twelve alias hypotheses hold, the retained
double rectangle, with its **entire** original Newton sum, has upper
rate \(B_1+\tau\) for every \(\tau>0\). At the actual
reference it has the nonzero packet
\[
 \frac{2\pi}{N^2}
 \frac{\widehat A_1(a_*,e_*,t_*,-2)}
      {\sqrt{\det(-\widehat{\mathcal F}_{1,(e,t)}'')}}
 e^{N\mathcal P_1(a_*)}(1+O(N^{-1})).
 \tag{13}
\]
The power is \(N^2N^{-3}(2\pi/N)=2\pi N^{-2}\).
All ordinary jets, parity choices and original Gaussian branches
are retained. A neighboring unselected type-four halfweight is
handled by its nonpositive convex Bregman remainder, exactly as
in the previous terminal comparison; this uses the actual negative
external height. No selected-neighbor statement is inferred.

The packet (5) is used pointwise on exact contours for their bounds,
and locally for the Gaussian symbol. No relative error is substituted
into a real outer sum and then assumed to remain relatively small
after cancellation. The physical complement in (2), outside the two
retained intervals, is not bounded by Proposition 2.

## 4. What convexity does not settle

The flattened tests require actual phase estimates. Even the full
Hessian bound and all quoted image boxes cannot imply their signs.
For a logical illustration, choose an attached critical coordinate
\(t_*=1/4-21i/200\), strictly within its proved rectangle,
and a separable quadratic phase with negative Hessian
\((\pi/50)I\). At the flattened left cut \(t=.15\), with
all other coordinates fixed at their critical values, its real phase
increases by
\[
 \frac\pi{100}\left\{(21/200)^2-(1/10)^2\right\}
                         =\frac{41\pi}{4000000}>0.
 \tag{14}
\]
This is a counterexample only to an inference from curvature and
boxes. It is not the original phase, an actual coupled endpoint root,
or a finite-source counterexample. The smaller \(e\)-alias
penalties in the reduced cycle likewise need proof; they cannot be
discarded because the inner coefficient has a packet.

For comparison, retaining the unreduced three-index rectangle gives
\(N^3\prod_{j=1}^3(I_j+A_j)\). After deforming unaliased
paths, there are \(9^3-3^3=702\) alias currents and
\(3^3=27\) constant-mode currents. A sufficient full-target
alias list has 24 singles, 24 doubles and eight triples: each
nonaliased height is independently zero or its actual value. The
zero-penalty flattened list has six one-cut faces, twelve two-cut
faces and eight corners. Separate height convexity reduces those
currents to these 56 plus 26 comparisons, but does not prove their
signs either. Equation (3) uses the already proved complete inner
source to remove this additional set of unestimated Newton currents.

No new parameter cover, root calculation, or numerical test is used
in this deduction. Neither conditional criterion proves the whole
type-four terminal source before its stated comparisons and exterior
estimates are supplied.
