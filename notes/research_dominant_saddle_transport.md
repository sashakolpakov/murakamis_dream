# Persistence of a dominant saddle and the conditions it needs

Research note, 2 November 2026. This note proves a continuation
principle for a controlled holomorphic period. It also gives an
explicit counterexample to replacing dominance along the path by
dominance at its two endpoints. It does not establish the required
global hypotheses for arbitrary short fillings.

The useful object is a one-dimensional relative homology group:
after contours supported at lower real action are discarded, the
selected saddle supplies one remaining generator. Transport
preserves its coefficient. Ordinary Stokes changes only add lower
generators to this one.

## 1. What the period and its leading coefficient mean

Let \(X_t\) be a complex manifold of dimension \(d\), depending
smoothly on \(t\in[0,1]\). Any poles or branch divisors have been
removed; alternatively, a specified covering has been chosen on
which the phase is single valued. Consider

\[
 I_N(t)=\int_{\Gamma_t}e^{Nf_t(z)}\omega_{N,t}(z),
 \qquad N\longrightarrow+\infty.
 \tag{1}
\]

Here \(f_t\) is holomorphic, \(\Gamma_t\) is an oriented real
\(d\)-cycle with permitted decaying ends, and
\(\omega_{N,t}\) is a holomorphic \(d\)-form on all chains used
in the argument. The cycle must be transported as a relative
homology class. Replacing it at each parameter by a convenient
real contour without recording crossed poles is a different
operation.

Write \(h_t=\operatorname{Re}f_t\). Suppose \(p(t)\) is a
nondegenerate critical point. Choose continuous local Morse
coordinates and the corresponding orientation so that

\[
 f_t=f_t(p(t))-\frac12(w_1^2+\cdots+w_d^2).
 \tag{2}
\]

Near \(p(t)\), suppose

\[
 \omega_{N,t}=
       \bigl(a_t(w)+O(N^{-1})\bigr)\,dw_1\cdots dw_d,
 \qquad a_t(0)\ne0,
 \tag{3}
\]

uniformly with the derivatives needed for the local integral.
In arbitrary original coordinates, \(a_t(0)\) includes the
chosen square root of the inverse Hessian determinant. Continuous
transport can change its orientation sign around a loop, but
cannot make it zero.

The integer multiplying the local descending cycle is denoted
\(k(t)\). It is distinct from \(a_t(0)\): the former comes from
the integration cycle, the latter from the integrand. Both must
be nonzero to obtain the usual nonzero leading term.

## 2. A precise controlled-transport hypothesis

A statement merely saying that the critical points remain finite
does not control the ends of a contour. The following are the
specific topological and analytic assumptions used below.

Choose continuous regular levels \(c(t)\) and \(\delta>0\) such
that

\[
 h_t(p(t))\ge c(t)+2\delta,
 \qquad
 h_t(q)\le c(t)-2\delta
 \quad\hbox{for every other critical point \(q\)}.
 \tag{4}
\]

Put \(A_t=\{h_t\le c(t)\}\), together with the permitted exit
ends. Require the following facts.
For homology, truncate each decaying end once it lies in
\(\{h_t<c(t)\}\); the remainder must be a finite chain whose
boundary lies in \(A_t\). Thus \(H_d(X_t,A_t;\mathbb Z)\)
below means ordinary relative homology of these truncated
chains, with the vanishing tail integrals restored afterwards.
No infinite formal sum of contours is included without a
separate convergence argument.

**Morse deformation above the cutoff.** Lowering \(h_t\) deforms
the region above \(A_t\) to \(A_t\) with one real \(d\)-handle,
the handle at \(p(t)\). There are no additional handles from
finite boundaries, deleted divisors, or infinity. The deformation
and this handle identification are uniform in \(t\).

This condition has a concrete flow formulation. Outside a small
Morse neighborhood, the normalized negative gradient has
\(dh_t/ds=-1\). Every part of a chain above the cutoff must follow
this flow until it reaches \(A_t\) or the Morse neighborhood,
without reaching a pole or escaping to infinity at finite
height. This must hold uniformly on finite height intervals.
Inside the Morse neighborhood, the quadratic model (2) attaches
exactly its descending \(d\)-disk. The corresponding parameter
transport of the level boundary and exit ends must also exist
without an escape. A proper Morse cobordism is one sufficient
way to verify these requirements. For a noncompact period,
they are facts to prove, not consequences of nondegeneracy.

**Transport of the original cycle.** The family of pairs
\((X_t,A_t)\) and the original admissible cycle classes have
compatible continuous identifications along the path. In
particular no pole is crossed, no unrecorded residue cycle is
added, and no integration boundary passes through the upper
region.

**Bounds on the lower chains.** The deformations of the original
cycle give lower chains \(R_t\) supported in \(A_t\), with
weighted integrability bounded by a power of \(N\). One precise
sufficient estimate is, for a fixed \(N_0>0\),

\[
       \int_{R_t} e^{N_0h_t}\lvert\omega_{N,t}\rvert
                      \le C N^b
 \tag{5}
\]

uniformly in \(t\). The portions of the selected descending
cycle outside its local Morse neighborhood satisfy the
corresponding estimate, with a fixed drop from \(h_t(p(t))\).
All Stokes deformations have vanishing boundary integrals at
the permitted ends. Polynomial volume growth and uniform
exponential decay at those ends can establish (5), but must
be checked for the particular period.

These hypotheses explicitly exclude a critical contribution at
an end whose real action is as large as that of \(p(t)\).
An exact cancellation showing that such an end represents no
cycle can also remove it; an upper bound on finite critical
values alone cannot.

## 3. The persistence theorem

**Theorem 1.** Under (2)--(5) and the controlled transport
hypotheses of Section 2, the selected cycle coefficient \(k(t)\)
is constant after its local orientation is transported. If
\(k(0)\ne0\), then

\[
 I_N(t)=
 k(0)\left(\frac{2\pi}{N}\right)^{d/2}
 a_t(0)e^{Nf_t(p(t))}
 \bigl(1+O(N^{-1})\bigr),
 \tag{6}
\]

uniformly on the compact parameter path. In particular the
leading coefficient never vanishes.

**Proof.** The Morse deformation identifies

\[
                  H_d(X_t,A_t;\mathbb Z)\simeq\mathbb Z.
 \tag{7}
\]

Indeed, outside the one critical neighborhood the normalized
flow lowers the height to the cutoff. In the quadratic model,
the change from the lower sublevel to the upper sublevel is
the attachment of one \(d\)-disk with its boundary already
in the lower sublevel. Its relative homology in degree \(d\)
has one generator. The no-escape condition ensures that
this procedure has not missed another component at a
divisor, finite boundary, or infinity.

The selected descending cycle \(J_t\) projects to that
generator. The original cycle projects to \(k(t)[J_t]\).
The identifications of pairs transport both classes
continuously. The integer \(k(t)\) is consequently locally
constant, and hence constant on the interval. This argument
uses the group (7), not a choice of a complete thimble basis
for all lower critical points.

Subtracting \(k(0)J_t\) from \(\Gamma_t\) gives a cycle whose
image in (7) is zero. Its integral therefore equals the
integral of a lower chain \(R_t\), up to boundaries on which
Stokes' theorem applies. The form \(e^{Nf_t}\omega_{N,t}\)
is closed: it is a holomorphic top-degree form. There are
no residue terms because the deformations stay in \(X_t\).
For \(N\ge N_0\), (5) gives

\[
 \left|\int_{R_t}e^{Nf_t}\omega_{N,t}\right|
       \le C N^b e^{(N-N_0)c(t)}.
 \tag{8}
\]

The selected cycle outside its local neighborhood has the
same type of exponentially smaller estimate. Inside it,
use (2), rescale \(w=N^{-1/2}v\), and integrate the Taylor
expansion in (3) against the real Gaussian. Odd terms
integrate to zero; the first relative error is \(O(N^{-1})\).
The leading integral is
\((2\pi/N)^{d/2}a_t(0)\).
Uniform nondegeneracy and compactness of the parameter
interval give a common neighborhood and common constants.
The strict gap (4) makes (8) exponentially smaller than
this nonzero term, proving (6). \(\square\)

This formulation separates the topological conclusion from
the analytic estimates. A proof of a relative homology
identification alone does not supply (5); a critical-value
inequality alone supplies neither.

## 4. Why ordinary Stokes walls do not remove a dominant term

There is an elementary equivalent description when the
descending cycles form a finite basis. A downward gradient
trajectory preserves \(\operatorname{Im}f\) and strictly
decreases \(\operatorname{Re}f\). An ordinary Stokes event
is a connection from one saddle \(p_h\) to another \(p_l\),
with

\[
 \operatorname{Im}f(p_h)=\operatorname{Im}f(p_l),
 \qquad
 \operatorname{Re}f(p_h)>\operatorname{Re}f(p_l).
 \tag{9}
\]

Assume this is an isolated connection, all critical points
remain nondegenerate, and no pole, boundary, or end event
occurs at the same parameter.

Cut the connecting descending cycle just before it enters
a Morse neighborhood of \(p_l\). On the two sides of the
wall, the two ways of continuing the cut differ by a local
descending disk at \(p_l\). Continuing that disk downwards
gives the lower descending cycle. Thus, with consistent
orientations,

\[
          J_h^+=J_h^-+mJ_l^-,
          \qquad J_l^+=J_l^-,
 \tag{10}
\]

where \(m\) is the signed count of the connections; at a
single transverse elementary event it is \(1\) or \(-1\).
Cycles not involved in the event are unchanged. This is
a cut-and-paste description of the usual Picard--Lefschetz
change, with its direction fixed by the decreasing real
action.

Writing the same transported cycle in the two bases gives

\[
          k_h^+=k_h^-,
          \qquad k_l^+=k_l^- -m k_h^-.
 \tag{11}
\]

It is the coefficient of the **lower** saddle that can
change. A strictly dominant saddle is never the lower
endpoint, so its coefficient survives every such wall.
The filtered proof in Section 3 avoids any difficulty
caused by several changes among lower saddles.

There is a useful weaker test: a selected coefficient can
change only when it receives a term from a higher saddle
whose coefficient is nonzero. One could prove persistence
by excluding these particular connections, without proving
that the selected saddle has the largest real value among
all critical points.

If every critical branch has one fixed strict real ordering
along a path, all these matrices preserve the same
triangular filtration. Their off-diagonal parts are
nilpotent. By contrast, knowing that each individual wall
matrix is unipotent is insufficient. Matrices

\[
 \begin{pmatrix}1&1\\0&1\end{pmatrix},
 \qquad
 \begin{pmatrix}1&0\\1&1\end{pmatrix}
 \tag{12}
\]

are individually unipotent, but their product has eigenvalues
\((3+\sqrt5)/2\) and \((3-\sqrt5)/2\). A common ordering,
or a common invariant one-dimensional quotient, is the
relevant extra property.

## 5. Endpoint dominance is insufficient: an entire cubic example

Let \(\Gamma\) run from infinity on the ray
\(\arg z=-\pi/3\) to the origin, then from the origin to
infinity on the ray \(\arg z=\pi/3\). Put

\[
 I_N(\lambda)=\int_\Gamma
      \exp\left[N\left(\frac{z^3}{3}-\lambda z\right)\right]\,dz,
 \qquad
 \lambda=e^{i\theta},\quad
 \frac{2\pi}{3}\le\theta\le2\pi.
 \tag{13}
\]

The contour is fixed. Its ends have uniform cubic decay
for all these \(\lambda\). The integrand is entire, and its
two critical points are distinct and nondegenerate
throughout the path. Continue the selected branch by

\[
       p(\theta)=e^{i\theta/2},
       \qquad
       f_\theta(p(\theta))
            =-\frac23e^{3i\theta/2}.
 \tag{14}
\]

At **both endpoints**, its critical value is \(2/3\);
the other critical value is \(-2/3\). Thus the selected
point is uniquely dominant at each endpoint, with the
same fixed gap \(4/3\).

At the first endpoint, substitute \(z=e^{i\pi/3}w\).
Then

\[
             f_\theta(z)=-\frac{w^3}{3}+w.
 \tag{15}
\]

The transformed contour consists of an incoming ray of
argument \(-2\pi/3\) and the positive real axis. On the
incoming ray \(w=re^{-2\pi i/3}\),
\(\operatorname{Re}f=-r^3/3-r/2\), so its integral is
\(O(N^{-1})\). On the positive real axis, the unique
maximum is at \(w=1\), with value \(2/3\) and second
derivative \(-2\). Ordinary real Gaussian estimation gives

\[
 I_N(e^{2\pi i/3})=
       e^{i\pi/3}\sqrt{\frac{\pi}{N}}\,
       e^{2N/3}\bigl(1+O(N^{-1})\bigr).
 \tag{16}
\]

At the final endpoint \(\lambda=1\), deform the contour
to the vertical line \(z=1+it\), oriented upwards.
This deformation is legitimate because the integrand is
entire. In the coordinate \(w=z-1\), the joining arcs
have \(\pi/3\le|\arg w|\le\pi/2\); both
\(\operatorname{Re}w^3\le0\) and
\(\operatorname{Re}w^2\le-\lvert w\rvert^2/2\) there,
so the large joining integrals tend to zero. On the
vertical line,

\[
     \frac{(1+it)^3}{3}-(1+it)
                =-\frac23-t^2-\frac{i t^3}{3}.
 \tag{17}
\]

Rescaling \(t=N^{-1/2}s\) gives

\[
 I_N(1)=
       i\sqrt{\frac{\pi}{N}}\,
       e^{-2N/3}\bigl(1+O(N^{-1})\bigr).
 \tag{18}
\]

The selected branch at this endpoint is \(p=-1\), with
value \(2/3\), but its coefficient is zero. The integral
comes from the other saddle \(p=1\).

There is no pole, amplitude zero, critical collision, or
change of the decaying ends in this example. The missing
hypothesis is precisely dominance along the path:
\(\operatorname{Re}f_\theta(p(\theta))<0\) for
\(\pi<\theta<5\pi/3\). At the interior ordinary Stokes
wall \(\theta=4\pi/3\), the selected saddle is the lower
one and its coefficient can change as in (11).
The endpoints lie on ordinary Stokes rays, but the real
gap and the displayed leading coefficients are
unambiguous. Small perturbations of the endpoints into
their adjacent sectors give the same example with
endpoints off those rays.

## 6. Other hypotheses that cannot be dropped

Nonzero cycle coefficient does not guarantee nonzero
leading amplitude. For example,

\[
 \int_{\mathbb R}(t+z)e^{-Nz^2}\,dz
                         =t\sqrt{\frac{\pi}{N}}
 \tag{19}
\]

has one nondegenerate saddle and fixed decaying ends, but
vanishes at \(t=0\). Here the local amplitude vanishes.

Poles can contribute a rate not represented by any
critical point. For \(f(z)=-z^2\), a small positively
oriented circle around \(z=i\) gives

\[
       \int_{|z-i|=\varepsilon}
                \frac{e^{-Nz^2}}{z-i}\,dz=2\pi i e^N.
 \tag{20}
\]

The only finite saddle has critical value zero. A
description using that saddle alone has omitted the
pole cycle. Moving poles or finite integration
boundaries require their corresponding terms to be
tracked just as explicitly.

Equal real actions also require a separate argument.
Two local Gaussian contributions with actions \(M\)
and \(M+i\pi\) and equal coefficients have sum

\[
       \sqrt{\frac{\pi}{N}}\,e^{NM}
                         \bigl(1+(-1)^N\bigr).
 \tag{21}
\]

Each local coefficient is nonzero, but the sum vanishes
at every odd integer level. One can realize (21) on
two components of a holomorphic period. The example
is relevant when different logarithmic lifts or
periodic aliases correspond to the same geometric
representation. A volume bound on representations
does not distinguish those lifts.

Finally, a family with \(N\)-dependent divisors, phase
branches, or cycles requires uniform versions of all
the hypotheses. The identity of its classical limiting
phase does not supply them. If a common top relative
homology line exists at every level, its coefficient
must be shown nonzero at every sufficiently large
level, with subexponential normalization; a computation
at one level is insufficient.

## 7. What representation-volume rigidity would supply

The papers of
[Francaviglia--Klaff](https://arxiv.org/abs/math/0411050)
and
[Francaviglia--Savini](https://arxiv.org/abs/1706.07347)
state rigidity results for representations of the
fundamental group of a **fixed complete finite-volume
hyperbolic manifold**. The latter also treats sequences
whose volumes approach the maximum. These are relevant
coverage references, not proofs imported into Theorem 1.

Even if those statements are independently verified,
applying them at an integer hyperbolic filling first
requires that every competing critical solution define
an actual representation of that filled group, and that
its real action equal the correctly normalized
representation volume. An exponential meridian
equation alone may not kill the full meridian matrix.
Uncalibrated action constants and logarithmic lifts
must also be accounted for.

After those checks, rigidity can help order the real
critical values **at that endpoint**. A compactness
statement for representations near maximal volume can
help exclude character-variety ends there. Neither
statement proves dominance along a deformation, as
the cubic example shows. Nor does character compactness
prove properness of a chosen quantum chart: decoration
coordinates or logarithmic lifts may escape while
the represented character stays bounded.

For a primitive cone deformation, the meridian
equation is

\[
                  U+pV=-2\pi i\lambda,
                  \qquad 0<\lambda<1.
 \tag{22}
\]

Such a representation generally belongs to the
unfilled exterior group; it does not factor through
the ordinary filled manifold group. Complete
representation-volume rigidity for the integer
filling therefore does not apply at these
intermediate parameters. Rigidity for the complete
parent would give the parent's volume as an upper
bound, whereas the geometric cone branch has already
decreased below that value. This does not compare a
competitor with the cone branch itself.

One would need a relative or cone-angle maximality
statement, with the same primitive constraints and
the correct boundary correction, or another proof
excluding incoming Stokes contributions to the
selected branch. In addition, the geometric branch
must remain nondegenerate along the chosen path.
Hyperbolicity of the final integer filling supplies
neither assertion.

The completed adjacent two-crossing calculation is
a useful warning. Its escaping alias has the same
real action as the finite geometric saddle, as
proved in
[the Bloch identity](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_alias_bloch_identity.md).
The successful proof removes that end by the
[exact full-circle cancellation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_pair_full_circle_bound.md).
It does not obtain a strict inequality between those
two critical values. A general period-continuation
approach must allow this kind of exact removal before
claiming that the remaining top relative group is
one-dimensional.

## 8. Attribution and the resulting research target

The Stokes interpretation by relative cycles and
intersection numbers is established asymptotic
analysis. A directly relevant reference, including
integration boundaries, is
[Delabaere--Howls, *Global asymptotics for multiple
integrals with boundaries*, Duke Mathematical Journal
112 (2002), 199--264](https://doi.org/10.1215/S0012-9074-02-11221-6).
Its
[institutional record](https://eprints.soton.ac.uk/29213/)
describes its treatment of generalized
Picard--Lefschetz changes and boundary contributions.
The arguments in Sections 3--5 were written directly
here; no theorem from that article is needed for them.

For the knot problem, the potentially useful general
theorem is now precise: construct the **actual**
period of the restored finite source, prove that its
top relative homology quotient is a transported line
after the genuine lower or null end cycles are removed,
and prove a nonzero local amplitude with uniform
subexponential normalization. A starting nonzero
coefficient would then survive by Theorem 1.

This could replace many separate contour certificates.
It has not yet been established for arbitrary short
fillings. Endpoint volume rigidity, or unipotence of
individual Stokes matrices, does not by itself supply
the missing transported line.

## 9. An exact analytic coupon family and the proved initializer

The [small-charge source theorem](research_small_charge_path_source.md)
now supplies an actual nonzero initial source on a fixed small
positive charge box. Its scope includes the original positive
paths, and the specified same-index finite graph sums treated
there. This does not initialize the source at charge zero.
The following interpolation makes the finite parameter family
precise without asserting that its top relative quotient has
been controlled.

Fix \(N\), put \(D=N-1,\ \eta=(-1)^D\), and use the original
physical angles and spectral variables
\[
 \tau_a=\frac{\pi(D-2a)}N,\qquad c_a=-2\cos\tau_a .
 \tag{23}
\]
For a complex parameter \(\chi\), let \(\mathcal C_{N,\chi}\)
be the unique polynomial of degree less than \(N\) with the
following full physical data. At a double root, choose either
of its angles \(\tau\ne0\) and set
\[
 \begin{split}
 \mathcal C_{N,\chi}(-2\cos\tau)
     &=\cos\bigl(N(1-\chi)\tau\bigr),\\
 \mathcal C_{N,\chi}'(-2\cos\tau)
     &=-\frac{N(1-\chi)\sin\bigl(N(1-\chi)\tau\bigr)}
                    {2\sin\tau}.
 \end{split}
 \tag{24}
\]
The two choices \(\tau,-\tau\) agree. At the simple odd-level
root \(-2\), prescribe the value one and no derivative.
Finite Hermite interpolation proves existence, uniqueness, and
entire dependence of every polynomial coefficient on \(\chi\).
At integral charges it gives the exact old coupons:
\[
 \mathcal C_{N,j/N}
   =\operatorname{rem}_{\,2T_N(w/2)+2}T_{N-j}(-w/2)
       \quad(0\le j\le N),\qquad
 \mathcal C_{N,0}=\eta,\quad \mathcal C_{N,1}=1 .
 \tag{25}
\]
For the endpoint at zero, use
\(\cos(N\tau_a)=\eta,\ \sin(N\tau_a)=0\);
the odd simple root also has \(\eta=1\).

Insert \(\mathcal C_{N,\chi_v}\) at each original traced
vertex, keeping the fixed original integer crossing powers.
The resulting finite source is entire in all the parameters.
The [exact trace contour](research_exact_complete_trace_contour.md)
continues to hold with angular representative
\(\cos(N(1-\chi_v)t_v)\). Its derivation uses only the full
physical jets and the oddness of the function being sampled;
it does not require this angular representative to be periodic.
Consequently, for each \(N\), the surrounding rectangles and
their grid-pole divisors can be chosen independent of
\(\boldsymbol\chi\). All vertical currents remain included.
This is an exact analytic family in the original algebra,
not a new assertion about a topological invariant at a
nonintegral charge.

In particular the all-zero-charge source equals \(\eta^m\)
times the uninserted source, where \(m\) is the number of
traced vertices. It is not a known complete bare-edge value.
At that endpoint the formal zero-charge central phase is even
in every selected angle, while each trace contributes its
odd factor \(\sin t_v\). Its symmetric local Gaussian
observation vanishes. The already proved initializer is
instead a box bounded away from zero.

There is no analogous cancellation from the companion at
the other endpoint. On a lower contour the exact scalar
kernel is
\[
 \frac{e^{-iNt}\cos(N(1-\chi)t)}
             {(1-\eta e^{-iNt})^2}
  =\frac12e^{-iN\chi t}
       \frac{1+e^{-2iN(1-\chi)t}}
                    {(1-\eta e^{-iNt})^2}.
 \tag{26}
\]
At \(\chi=1\) the numerator becomes two, restoring the
coefficient one of the original unit-charge trace.
More quantitatively, on a compact neighborhood with
\(|\Re t|\le A,\ -\Im t\ge h_0>0\), the numerator is
uniformly nonzero for real \(0<\chi\le1\), at every \(N\).
Indeed put \(s=N(1-\chi)\ge0\). For \(A>0\), set
\(s_0=\pi/(4A)\). If \(s\le s_0\) the exponential
\(e^{-2ist}\) has nonnegative real part, so the numerator
has modulus at least one. If \(s\ge s_0\), its modulus is
at least \(1-e^{-2s_0h_0}>0\). The case \(A=0\) is immediate.
Every fixed derivative in \(t\) is uniformly bounded, using
\[
              \sup_{s\ge0}s^k e^{-2s h_0}<\infty .
 \tag{27}
\]
The denominator in (26) and its derivatives are likewise
uniformly controlled on this neighborhood.

The transition layer \(1-\chi=O(N^{-1})\) must nevertheless
retain its \(N\)-dependent factor \(1+e^{-2ist}\).
It does not have one \(N\)-independent limiting amplitude
uniformly through \(\chi=1\). The local proof of Theorem 1
has the following direct variant: one may replace \(a_t\)
in (3) by \(a_{N,t}\) if its spatial holomorphic derivatives
are uniformly bounded and \(|a_{N,t}(0)|\) has a uniform
positive lower bound. The same Gaussian Taylor proof gives
(6) with \(a_{N,t}(0)\), with the same relative
\(O(N^{-1})\) error. No derivative bound in the external
parameter is required for this local estimate. Formula
(26) satisfies this local amplitude requirement wherever
the remaining actual source factors do.

Thus an exact analytic finite family and a nonzero starting
observation are now available. The Stokes conclusion of
Sections 3--4 is unchanged: a flat top relative line keeps
its coefficient through ordinary lower-saddle Stokes events,
without a scalar almost-invariance defect estimate.
What is still missing for general charge continuation is
a uniform identification of that line for the actual
\(N\)-dependent quantum period. In particular one must
control all competing cycles, including divisor and infinity
cycles, and verify the lower-chain bounds of Section 2.
The finite edge kernels cannot simply be placed in a
subexponential amplitude on an unproved global geometric
contour. Fixed grid poles in the trace representation do
not settle the other ends or aliases of a factorial-wire
representation. Analyticity of the coupons and strict
positivity of the geometric critical point alone do not
discharge these conditions.
