# Actual coherent cycles and the complex crossing graph

Research note, 6 November 2026. The positive coherent resolution of
the original finite head does not make its signed crossing a real
elliptic Fourier-integral transport on that resolution's real
phase space. A single original positive crossing already leaves
the real locus, on a bounded regular open set at complete color.
This is an explicit source-coordinate statement, not an abstract
Stokes example or a claim that the geometric contribution vanishes.

There is also an exact repair at the level of contours. Any regular
complex coherent point lies on an adapted positive coherent sphere
in the same source homology class. These spheres preserve every
finite contraction and can be chosen along bounded regular
transported data. Their allowable tangent planes and their
exponential metric conditioning identify what must still be
proved for a nonzero geometric saddle contribution.

## 1. The real locus is fixed by the original source

Use the balanced head and the exact compact resolution of
[the coherent-source period, Sections 1–2](compact_coherent_source_period.md).
Put \(n=N-1\), with metric
\[
 G_{jj}=\binom nj^{-1},\qquad
 \Gamma=\{(w,z):z=\overline w\}\subset
 X=(\mathbb P^1\times\mathbb P^1)\setminus\{1+wz=0\}.
 \tag{1}
\]
The actual normalized trace is the integral over this compact
sphere. Products insert one factor \(N\) per coherent resolution;
turns, pivots, boundary vectors and the modified-dimension line
remain the original ones.

Away from the two endpoint walls, its physical principal
coordinates are, with the original color \(M\),
\[
 t=\frac{wz}{1+wz},\qquad
 A=e^{2\pi i t},\qquad
 K=-M A^{-1},\qquad
 e=(MA^{-1}-M^{-1})/w,\qquad
 f=(1-A)w.
 \tag{2}
\]
These are precisely the actual balanced Gauss symbols proved
in the same note, Sections 4–5. On \(\Gamma\),
\[
             0<t<1,\qquad |K|=|M|.
 \tag{3}
\]
The endpoint terms omitted from the interior formula (2)
remain explicit in the finite coherent kernel; none is
discarded in the exact contour statements below.

There is an exact Hilbert-space counterpart to (3). The finite
matrix \(K_N=-(M/q_N)\operatorname{diag}(Q_N^{-j})\) is
\(|M|\) times a \(G\)-unitary matrix. For every vector \(\xi\)
and every complex \(\kappa\),
\[
 \|(K_N-\kappa)\xi\|_G
       \ge \bigl||\kappa|-|M|\bigr|\,\|\xi\|_G .
 \tag{4}
\]
This follows from the reverse triangle inequality, with no
asymptotic assumption. A normalized positive-metric state
cannot be an approximate \(K_N\)-eigenstate at a fixed
symbol outside the circle (3).

## 2. One original crossing leaves this real locus

The forward physical canonical map of the actual positive
crossing is
\[
 d=1-e_1f_2,\qquad K'_1=K_2d,\qquad K'_2=K_1/d.
 \tag{5}
\]
All its other entries and its inverse are the rational
expressions in
[marked braid holonomy, Section 4](marked_braid_holonomy.md).
This is the forward kernel relation; the point map for
quantum pullback is its inverse, as explained in
[regular holonomy braiding, Sections 1–2](regular_holonomy_braiding.md).

Take complete colors \(M_1=M_2=1\) and the two real coherent
points
\[
 w_1=z_1=1,\qquad
 w_2=z_2=1/\sqrt3 .
 \tag{6}
\]
Then \(t_1=1/2,\ t_2=1/4\), and
\[
 A_1=-1,\quad A_2=i,\quad
 (K_1,e_1,f_1)=(1,-2,2),\quad
 (K_2,e_2,f_2)
       =\left(i,-\sqrt3(1+i),(1-i)/\sqrt3\right).
 \tag{7}
\]
Writing \(r=2/\sqrt3\), (5) gives
\[
 d=1+r-ir,\qquad
 K'_1=r+i(1+r),\qquad
 |K'_1|^2=\frac{11}{3}+\frac4{\sqrt3}>4.
 \tag{8}
\]
The output therefore fails (3), by a fixed margin.

This point belongs to a regular source chart. In the actual
positive-crossing generating relation the transfer variable is
\(C=1/d\), and the five factors use
\[
                  A_2=i,\quad C=1/d,\quad A_1^{-1}=-1,
                       \quad A_2C=i/d,\quad A_1^{-1}C=-1/d .
 \tag{9}
\]
Every displayed argument is nonzero and different from one;
\(d\ne0\), and both \(K_i\) are units. The rational inverse
is regular at the image because it is the inverse of (5)
on this chart. The input positions are away from both head
endpoints and from total position \(t_1+t_2=1\).

For an independent check of the physical order, put
\[
 G_i=\begin{pmatrix}K_i&e_i\\K_if_i&K_i^{-1}+e_if_i\end{pmatrix},
 \qquad
 b_{-,i}=\begin{pmatrix}1&0\\-K_if_i&K_i\end{pmatrix}.
 \tag{10}
\]
The ordered meridians are
\(H_1=G_1,\ H_2=b_{-,1}^{-1}G_2b_{-,1}\).
The original positive map is
\((H_1,H_2)\mapsto(H_1^{-1}H_2H_1,H_1)\).
Here \(b_{-,1}G_1=\left(\begin{smallmatrix}1&-2\\0&1\end{smallmatrix}\right)\);
conjugating \(G_2\) by this matrix gives its first diagonal
entry exactly as in (8). No independent \(G_2\) was substituted
for the prefixed second meridian.

All matrices, their inverses, and the factors in (9) remain
bounded and nonzero on a sufficiently small compact
neighborhood. The strict modulus failure persists there,
also for meridians in a fixed neighborhood of \(M_i=1\).
Thus this is a local open-set obstruction at bounded
transported meridians, rather than an escaping-source example.

**Conclusion.** Invertibility of the original local
holomorphic symbol and Hurwitz transversality do not make
the crossing a real canonical graph on \(\Gamma\times\Gamma\).
Equation (4) makes the distinction detectable in the exact
positive head metric. This rules out that proposed automatic
real-wavefront propagation argument. It does not rule out
complex analytic packets, nonunitary transport, or a
contributing complex saddle of the actual finite source.

## 3. Adapted positive spheres retain the exact contraction

The surface \(X\) is also the space of rank-one idempotents
of trace one on \(\mathbb C^2\). On the displayed chart,
\[
 P(w,z)=\frac1{1+wz}
       \begin{pmatrix}1&w\\z&zw\end{pmatrix}.
 \tag{11}
\]
The sphere \(\Gamma\) consists of the Hermitian idempotents.
Every \(P_*\in X\) is \(gP_0g^{-1}\), with
\(P_0=\operatorname{diag}(1,0)\) and \(g\in\mathrm{GL}_2(\mathbb C)\):
choose one nonzero vector in its image and one in its kernel.
Consequently
\[
                       \Gamma_g=g\Gamma g^{-1}
 \tag{12}
\]
is a compact sphere through \(P_*\).

Let \(\rho_n=\operatorname{Sym}^n\) in the original binomial
head convention. Its rank-one projector
\(\Pi_N(P)=\rho_n(P)\) is exactly the coherent projector used
in the trace formula:
\(\sigma_A(P)=\operatorname{Tr}(A\Pi_N(P))\).
The invariant two-form \(\omega_I\) from the coherent-source
note satisfies
\[
 N\int_{\Gamma_g}\Pi_N(P)\,\omega_I(P)=I,\qquad
 \int_{\Gamma_g}\sigma_A\,\omega_I=\frac{\operatorname{Tr}A}{N}.
 \tag{13}
\]
Indeed conjugation by \(g\) preserves the polar divisor and
\(\omega_I\); pullback changes the operator to
\(\rho_n(g)^{-1}A\rho_n(g)\). The known identity resolution
on \(\Gamma\) proves (13).
Equivalently a path in the connected group
\(\mathrm{GL}_2(\mathbb C)\) gives a compact homology between
these cycles in \(X\), with no polar crossing.
At each fixed physical level the head kernels are polynomial
sections; their only head-coordinate poles in this exact
calculus are the displayed resolution divisors. Apparent
divisors of a chosen asymptotic phase do not invalidate this
finite identity, but crossing them can invalidate that phase's
uniform asymptotic description.

Insert (13) separately at every internal edge of an original
finite tensor contraction. This represents the same scalar
over any product of adapted spheres, with exactly the same
factor \(N\) for each resolution. Opposite frame matrices
cancel on each internal edge. External vectors, covectors,
turns and marked source operators transform covariantly;
they are not replaced by normalized traces. For example
\(\ell Av=\operatorname{Tr}(v\ell A)\), so the corresponding
trace period has its literal outside factor \(N\).
For the normalized diagonal knot cut, the original
conservation identity already permits
\(\operatorname{Tr}A/N\), as in the source note.

If the original lifted critical points remain in a compact
regular part of \(X\), the image/kernel choices for \(g\)
can be made bounded with bounded inverses locally, or along
a fixed compact parameter interval. Locally this follows
by choosing two fixed coordinate minors that stay nonzero;
along an interval such choices can be continued and covered
by finitely many regular charts. Thus (13) legitimately
places a regular complex critical configuration on a
representative of the original product cycle. It does not
change its source class.

## 4. Bounded frames do not give a bounded Hilbert cost

The sphere \(\Gamma_g\) is positive for the head metric
\[
        G_g=\rho_n(g)^{-*}G\,\rho_n(g)^{-1}.
 \tag{14}
\]
It is a genuine positive coherent resolution in that metric.
However its conditioning relative to the original metric is
exponential. If the two singular values of \(g\) in the
standard two-dimensional metric are \(s_1\ge s_2>0\), the
singular values of its symmetric power are
\(s_1^{\,n-j}s_2^j\). Hence exactly
\[
       \|\rho_n(g)\|_G=s_1^n,\qquad
       \|\rho_n(g)^{-1}\|_G=s_2^{-n},\qquad
       \operatorname{cond}_G\rho_n(g)
             =(s_1/s_2)^{N-1}.                            \tag{15}
\]
The binomial metric is the induced symmetric-tensor metric,
so the ordinary singular-value decomposition proves these
formulas directly.

For the full scalar contraction these factors cancel
algebraically, as in (13). A proof that cuts the word and
uses separate positive norm estimates must instead retain
them in its exponential action budget. Bounded meridians
and bounded \(g\) are therefore insufficient to declare
this change of polarization subexponential.

## 5. The remaining local source test on the adapted cycles

The allowable positive tangent planes are constrained.
After a fixed frame sends \(P_*\) to \(P_0\), every other
frame doing so differs by an invertible diagonal matrix.
Any adapted sphere containing \(P_0\) can be represented this
way: first right-multiply its frame by a unitary matrix
sending \(P_0\) to the relevant point of \(\Gamma\).
Its sphere through \(P_0\), in the local coordinates of
(11), has tangent
\[
                         z=\lambda\overline w,\qquad
                                  \lambda>0.
 \tag{16}
\]
For example conjugation by
\(\operatorname{diag}(a,b)\) sends
\(w\) to \((a/b)w\) and \(z\) to \((b/a)z\);
on the transformed real sphere the multiplier is
\(|b/a|^2\). This proves (16), including its positivity.

For several wires put \(D=\operatorname{diag}(\lambda_j)>0\).
Suppose the **original assembled local phase**, in these
fixed regular coordinates, has critical Hessian
\[
                    \begin{pmatrix}A&B\\B^t&C\end{pmatrix},
                  \qquad A=A^t,\quad C=C^t.
 \tag{17}
\]
Its real quadratic form on the product tangent (16) is
one half of
\[
 \operatorname{Re}\left[
 w^t(A+D\overline C D)w+
                   2w^tBD\,\overline w\right].
 \tag{18}
\]
Thus a strict real maximum on one of these positive product
cycles requires negativity of this particular form for some
positive diagonal \(D\). Complex nondegeneracy alone is not
that condition. For instance restriction to a single wire
requires
\[
 2\lambda_j\operatorname{Re}B_{jj}
       +\left|A_{jj}+\lambda_j^2\overline{C_{jj}}\right|<0.
 \tag{19}
\]
The inequalities are tests of the actual source Hessian,
not conclusions inferred from a transverse character-variety
intersection.

Suppose separately that (18) is uniformly negative, that the
actual whole integrand admits a local phase expansion with
nonzero leading amplitude on this product cycle, and that
the remainder of this **same exact contraction** has a
strict calibrated upper-rate gap. Then the ordinary
local Gaussian integral has nonzero coefficient and the
complement cannot cancel it. All three clauses are needed.
The coefficient is then obtained on a specified literal
source representative, without an assumed separately
invariant saddle sector. A formal symbol alone does not
supply the whole-integrand expansion or its remainder bound.

This identifies a concrete route for bounded transported
meridians: use (13) to choose legitimate cycles through
the original marked critical configuration, verify the
restricted Hessian test (18), and control the original
finite contraction away from that configuration, retaining
the endpoint walls and the costs (15). The existing
canonical/critical correspondence does not yet prove those
source inequalities for arbitrary fixed short words.
No assertion about a nonzero geometric coefficient, its
absolute volume action, or the finite-exception theorem
is made from Hilbert positivity alone.
