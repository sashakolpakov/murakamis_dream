# A full one-boundary packet radius from the frozen three-crossing certificate

Private written quantitative deduction, 9 November 2026. The original
trace-first certificate determines an eligible radius for the complete
canonical polynomial \(Q_N(u)=P_{3,N}(0,u)\). The radius below is an
explicit expression in its frozen interval endpoints. No interval
endpoint is reevaluated, combined numerically, or replaced by a new
root proposal in this note.

The result concerns the full source, including both parity conventions,
every discarded Newton group, all contour currents and the original
Hermite normals. It does not use a shortened-edge packet. The resulting
radius can be very small; no adequate attachment-action budget follows.

## 1. Fixed data and an unevaluated radius formula

Use the power-three entry of the original
[degree-two certificate record](../repro/results/research-internal-degree-two-contours.json).
Its mathematical interpretation and finite-source scope are those of
[the certificate proof](research_internal_degree_two_contour_certificates.md)
and [the full single-vertex theorem](research_all_nonzero_degree_two_fillings.md).
Keep the exact selected point
\[
 x_*=\xi_*+ih_x,\qquad t_*=\tau_*-ih_t,\qquad
 p_*=(x_*,x_*,t_*),\qquad M_3=\Re S_3(0,0).
 \tag{1}
\]
Write the frozen local rectangle, in its recorded coordinates, as
\[
 Q=[q_1,q_2]\times[q_3,q_4],
       \qquad(\xi,\tau/(2\pi))\in Q.
 \tag{2}
\]
Let
\[
 \begin{split}
 X&=[x_-,x_+]+i[h_-,h_+],\\
 T&=[t_-,t_+]-i[H_-,H_+]
 \end{split}
 \tag{3}
\]
be the recorded selected-wire and selected-angle enclosures.
All endpoints in (3) mean the exact rational endpoints of the
printed outward decimal balls. Let \(d_{\rm H}>0\) be the lower
endpoint of the recorded lower bound on the determinant of the real
scaled Hessian. The local certificate also proves its \(xx\) entry
strictly negative throughout \(Q\).

Define the following positive, fixed numbers by the indicated
expressions; they are not evaluated here:
\[
 \sigma=\frac{d_{\rm H}}2,
 \tag{4}
\]
\[
 \begin{split}
 \eta=\frac12\min\biggl\{&
 \frac1{64},\,h_-,\,\frac{H_-}{2\pi}-h_+,\\
 &x_--q_1,\ q_2-x_+,\ 
       \frac{t_-}{2\pi}-q_3,\ q_4-\frac{t_+}{2\pi},\\
 &\frac12-x_+-\frac{t_+}{2\pi},\
       \frac{t_-}{2\pi},\
       \frac12-\frac{t_+}{2\pi},\
       x_-,\ \frac12-x_+\biggr\}.
 \end{split}
 \tag{5}
\]
The strict root, bulk and local-rectangle checks in the frozen
certificate are exactly the positivity guards used in (4)--(5).
Thus these formulas use quantitative data already certified by that
record, rather than a new assertion that a sufficiently small radius
exists. The only nonrational universal constant occurring in (5)
is the original \(\pi\). A rational lower replacement is possible,
but is unnecessary for the written statement.

Set
\[
 B=2^{50}\eta^{-6},\qquad
 \mu=\min\{1,\sigma/(4B)\},\qquad d=\eta/64,
 \qquad \ell=\min\{d/8,\mu/(16B)\},
 \tag{6}
\]
\[
 g_0=\min\{1/40\,000\,000,\ \mu d^2/64,\ \eta/64\},
 \tag{7}
\]
and finally
\[
 \boxed{\quad
 r_{\rm full}=\frac12\min\left\{
 \frac1{64},\ \frac{\ell}{16},\
 \frac{\mu\ell}{16B},\
 \frac{\mu^2}{64B^2},\
 \frac{g_0\mu}{64B^2},\
 \frac{g_0}{16}\right\}>0 .
 \quad}
 \tag{8}
\]
Every quantity in (8) is now specified by the frozen record and
elementary operations. Formula (8) is not an assignment of a decimal
or dyadic numerical value to the radius.

**Theorem.** On a neighborhood of the closed disk
\(\{|u|\le r_{\rm full}\}\), the full canonical source satisfies
\[
 Q_N(u)=C_{N,3}N^{-3/2}A_3(0,u)e^{NS_3(0,u)}
                      \{1+O_{\rm hol}(N^{-1})\},
 \qquad C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
 \tag{9}
\]
The phase and nonzero amplitude are the original ones. The estimate
is uniform through both parities, and every fixed derivative of the
normalized remainder has the same order on smaller disks. In
particular \(r_{\rm full}\) is an eligible full-source radius for
[the whole-frequency constant audit](research_mixed_next_whole_frequency_constant_audit.md).

## 2. Uniform elementary bounds on the unchanged surfaces

The exact internal phase for the one-free-boundary source is
\[
 \begin{split}
 F(\mathbf z,u)
  ={}&b(x_1,t)+b(x_1,0)+b(x_2,t)+b(x_2,u)
                         +\frac{3it^2}{4\pi}-it,\\
 &\mathbf z=(x_1,x_2,t).
 \end{split}
 \tag{10}
\]
It retains the original sidewise \(J_\pm\) primitives. Only the
last free factor changes when \(u\) changes.

On every one of the nineteen fixed surfaces,
\(\alpha\le\Re x\le\beta\), where
\(\alpha=1/32,\ \beta=15/32\), and
\(|\Im x|\le h_x<1/(2\pi)\).
For \(|u|\le1/64\), the free factorial arguments
\[
 \frac12\pm\frac{u}{2\pi},
 \qquad \frac12-x\pm\frac{u}{2\pi}
 \tag{11}
\]
have real parts strictly between \(1/64\) and \(1-1/64\).
Consequently this perturbation crosses no free-factorial cut,
including on a lower wire or a nested endpoint. The exact difference
\[
 R(\mathbf z,u)=F(\mathbf z,u)-F(\mathbf z,0)
                        =b(x_2,u)-b(x_2,0)
 \tag{12}
\]
is holomorphic and even in \(u\). On all those fixed surfaces,
\[
                         |R(\mathbf z,u)|\le B|u|^2 .
 \tag{13}
\]

Here and below \(B\) deliberately bounds more derivatives than are
needed. We give elementary bounds to specify its role. For
\(w=r+is\) in the continued primitive domains, use
\[
 |\sin\pi w|^2=\sin^2(\pi r)+\sinh^2(\pi s),\quad
 J''(w)=\pi\cot\pi w,\quad
 J'''(w)=-\pi^2\csc^2\pi w,
 \tag{14}
\]
\[
 J^{(4)}(w)=2\pi^3\cot\pi w\,\csc^2\pi w.
 \tag{15}
\]
On the lifted \(Q\) and its internal complex neighborhood of radius
\(\eta/16\), the nonconstant internal factorial arguments have imaginary distance
at least \(\eta/2\) from their real zeros. This follows from the
two separate guards \(h_x\ge2\eta\) and
\(h_t/(2\pi)-h_x\ge2\eta\) in (5).
For the free arguments (11), use instead their real-part distance.
Every relevant primitive argument has imaginary part of modulus less
than one: the original cubic continuation gives \(h_t<1\) and
\(h_x<1/(2\pi)\), so the normalized internal arguments are bounded
by \(1/\pi+2\eta<1\), also on the indicated neighborhood.

Thus one can use
\[
 |\sin\pi w|\ge\eta/4,\qquad |\cos\pi w|<64.
 \tag{16}
\]
The continued first logarithmic derivative is bounded by
\(100/\eta\); its possible original sidewise linear terms are included.
For example this follows by bounding the logarithm of
\(2\sin\pi w\) above and below using (16), with argument variation
less than \(4\pi\) on the stated one-period domains.
Equations (14)--(16) bound the next three derivatives by
fixed powers of \(\eta^{-1}\). In particular the fourth is less than
\(2^{19}\eta^{-3}\). There are at most twenty-four primitive
coefficients in (10), counted with multiplicity. Their affine
argument coefficients have modulus at most one; replacing every
entrywise bound by the Euclidean tensor norm costs less than
\(4^4\). The crossing term has only two nonzero derivative orders.
These estimates are all smaller than \(B\) in (6).

The resulting bounds, on the stated neighborhoods, include
\[
 \begin{gathered}
 \|\nabla_{\mathbf z}F(\mathbf z,0)\|\le B,\quad
 \|D^2_{\mathbf z}F(\mathbf z,0)\|\le B,\quad
 \|D^3_{\mathbf z}F(\mathbf z,0)\|\le B,\\
 \|\nabla_{\mathbf z}R(\mathbf z,u)\|\le B|u|^2,\qquad
 \|D^2_{\mathbf z}R(\mathbf z,u)\|\le B|u|^2 .
 \end{gathered}
 \tag{17}
\]
For the last line use evenness and the mixed derivatives through
total order four. This also proves (13), without evaluating a
primitive at a new point.

The scaled Hessian entries on \(Q\) have modulus at most \(B\).
Since its negative real Hessian is positive definite and has
determinant at least \(2\sigma\), its smaller eigenvalue is at least
\(\sigma/B\); the weaker bound \(\sigma/(2B)\) is sufficient.
The exact lifted identity
\[
 \Re D^2F(\mathbf z,0)[(v_1,v_2,w)]^2
  =\frac12\sum_{j=1}^2
       \Re D^2\Psi_3(x_j,t)[(v_j,w)]^2
 \tag{18}
\]
therefore gives
\[
                    -\Re D^2F(\mathbf z,0)\succeq\mu I
 \tag{19}
\]
throughout the lifted real local region. This is the full
three-variable quadratic form, not an entrywise Schur estimate.

## 3. The critical point and the translated local cube

Put \(H_0=D^2F(p_*,0)\). Exact stationarity is one of the
original logarithmic checks. By (19),
\[
                          \|H_0^{-1}\|\le\mu^{-1}.
 \tag{20}
\]
For \(|u|\le2r_{\rm full}\), consider
\[
             \mathcal T_u(\mathbf z)
                  =\mathbf z-H_0^{-1}\nabla_{\mathbf z}F(\mathbf z,u).
 \tag{21}
\]
On the ball \(\|\mathbf z-p_*\|\le\ell\), (17) and (8) give
\[
 \|D\mathcal T_u\|
       \le\mu^{-1}\{B\ell+B|u|^2\}<1/8,\qquad
 \|\mathcal T_u(p_*)-p_*\|\le B|u|^2/\mu.
 \tag{22}
\]
Every entry of the minimum in (8) is at most one, so
\(|u|^2\) is bounded by each of the displayed entries as well.
The contraction consequently has a unique fixed point \(p(u)\),
holomorphic in \(u\), and
\[
 \Delta(u)=p(u)-p_*,
 \qquad \|\Delta(u)\|\le2B|u|^2/\mu\le\ell/8 .
 \tag{23}
\]
This is the original critical branch by uniqueness at zero.
Taylor expansion at its exactly stationary starting point gives
\[
 |F(p(u),u)-F(p_*,0)|\le2B|u|^2.
 \tag{24}
\]

Let \(\mathcal C=p_*+[-d,d]^3\) be the original real-direction
cube inside the selected horizontal contour. The guards in (5)
put it strictly inside the lifted local region. On the real
boundary of this cube, (19) gives
\[
                     \Re F(\mathbf z,0)\le M_3-\mu d^2/2.
 \tag{25}
\]
Translate the cube to \(p(u)+[-d,d]^3\), one coordinate at a
time. The exact leading integrand is holomorphic throughout this
local deformation. The resulting side faces retain their actual
orientations. A point of any such face differs by at most
\(\|\Delta(u)\|\) from a point on the original cube boundary.
By (13), (17), (23), its real phase differs from that original
boundary phase by at most
\[
 B|u|^2+B\|\Delta(u)\|
                  \le3B^2|u|^2/\mu\le3g_0/64 .
 \tag{26}
\]
Together with (24)--(25), this pays every added face with a fixed
gap relative to \(\Re F(p(u),u)\).

On the translated cube the real Hessian remains negative definite.
Indeed its change from (19) is at most
\[
 B\|\Delta(u)\|+B|u|^2<\mu/2.
 \tag{27}
\]
The selected point is its only stationary maximum. Its factorial
arguments remain in the ordinary nonzero bulk: (5) supplies the
strict positive real margin, and \(d+\|\Delta(u)\|<\eta/32\).
The sine factors in the original density and the full Hessian
determinant remain nonzero for the same reason and by (27).
The Gaussian square root therefore continues with its original
orientation and sign.

## 4. The complement and every original finite source

The original scaled main gap outside \(Q\) is \(10^{-7}\).
In the full two-wire source it is at least \(10^{-7}/2\), by
the exact average identity (18) for the phase itself. Inside the
lifted \(Q\), but outside \(\mathcal C\), integration of (19)
gives the gap \(\mu d^2/2\). The remaining eighteen certified
surfaces, including all independent nested endpoint heights,
have larger positive gaps. The upper-wire correction has loss
\(2\pi h_x\), and all nonleading angular charges have loss at
least \(h_t\). Both exceed the weaker margin \(\eta\) used in (7).

The perturbation in (13) changes none of their factorial sides,
Fourier charges, endpoint orientations, rational denominators,
or integration heights. Equations (7)--(8),(24) preserve a gap
at least \(g_0\) for every such nonlocal group. In particular
one does not replace the complete rational alias factor by a
single charge before it is bounded.

There are also the two original groups discarded before these
nineteen surface estimates. On real free angles, the full wire
tails, including high Newton indices and all first normals,
have gap greater than \(1/4\). The full outer angular nodes,
with every retained subset eligible, have rate less than
\(8/5<M_3-1/5\). These are the separate estimates in Section 4
of the full single-vertex theorem.

Each complete discarded group is a polynomial of degree at most
\(D=N-1\) in \(-2\cos u\). Its uniform real-angle bound therefore
extends at a cost no greater than
\[
                     (2D+1)e^{D|\Im u|}.
 \tag{28}
\]
One way to see (28) is to expand in the cosine basis and use the
real-interval norm to bound each coefficient; each cosine mode
costs at most \(e^{D|\Im u|}\).
This uses the norm of the original discarded group, including
its Hermite trace. It does not infer a bound for its summands
from a coherent cancellation. Since \(2r_{\rm full}\le g_0/16\),
these two discarded gaps persist relative to (24).

The same argument treats the unexpanded collar of angular height
at most \(1/N\). Its real-free-angle source has the original
outer-angle bound; the degree estimate (28) is applied before
any wire expansion. The already proved \(O(N^{-1/2})\) continuation
cost of that collar and its polynomial trace factors preserve
the fixed gap for all sufficiently large \(N\).

All finite factorial domains remain the original ones. On the
large surfaces only the free arguments (11) move, and they stay
in their positive strip. The internal reciprocal factorials keep
both terms of their prescribed reflection formula, including
their moving zeros. Near the translated saddle their ordinary
bulk expansion is uniform, with the exact half-step shifts and
density
\[
 \prod_{j=1}^2
  \frac{1}{4N^2\sin^2(\pi x_j)} .
 \tag{29}
\]
The original \(O(N^{-1})\) half-grid changes have the same
zero-safe \(O(\log N)\) exponent errors as before. They alter
neither the radius nor any source inventory.

Apply holomorphic stationary phase on the translated cube.
Equations (25)--(28) pay its complement and every new side face.
The unchanged two wire sums, full trace and three-dimensional
Gaussian give exactly \(C_{N,3}N^{-3/2}\). The coefficient is
the original formula
\[
 A_3(0,u)=\frac{i(2\pi)^{3/2}}{16\pi}
 \frac{\sin t(u)}
 {\sin^2(\pi x_1(u))\sin^2(\pi x_2(u))
                         \sqrt{\det(-D^2F(p(u),u))}} .
 \tag{30}
\]
It is holomorphic and nonzero. This proves (9) uniformly on the
closed disk of radius \(r_{\rm full}\), with holomorphic
normalization on the larger disk used above. Cauchy's formula
then gives the fixed-derivative assertion.

## 5. Quantitative scope

The formula (8) removes the need to assign an unjustified arbitrary
small number to the full-packet radius. Its input consists of
specific frozen certificate margins; every dependence is displayed.
It does not evaluate those margins, produce a decimal radius, bound
the attachment excess, or show that the resulting whole-frequency
gain is adequate. The earlier root-isolation radius \(2^{-100}\)
is never substituted for \(r_{\rm full}\).

No numerical evaluation, import, compilation, certificate replay,
saved-value arithmetic, or change to a frozen source was used.

## Frozen sources

- Full single-vertex source:
  7ac634d458e5805e95a7ce064d4e1fc513c96c0b758cfaee9f91fd46de10304c.
- Original certificate proof:
  954ff66b16b74aaa24a107cd2184a774ec7a0f97acf7d58d8f8aabd1a58288ec.
- Trace-first lifting:
  b1a9429031499098756b725757f54c46b7fdaa4033845f1dc56fa162ec80aa10.
- Uniform factorial estimates:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Full outer-angle estimate:
  239cc1034f36217971c831d7bf5f8b6e6bf252a5988d6adf82f2106ec2c62b50.
- Original cubic continuation:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Original certificate checker:
  5f9d19c803f0763b448063055ec33852dfb29559031a620b45d97bc720fb30c1.
- Original interval engine:
  a89cf8c782c1c782a644cfb59e6586a9a07db36c82653e65363d6b74cea0bef0.
- Original certificate record:
  22a4af3e274339b54fd2f4eaf475c22edf84858b9368b930bb1df615a5bafe11.

