# The actual meridian family of the opened complex packet

Private written proof, 19 November 2026.

The complex-clock packet in C has an actual holomorphic meridian
extension with all packet, carrier, frame, and window marks held
fixed. Its entire meridian dependence is an exact translation of
C's three tilt parameters. Consequently the same finite residue
cycle has a nonzero saddle coefficient on a fixed complex
meridian neighborhood, with all mixed jets and annular currents.
The zero-framed first normal is nonzero on an explicit open
subchart. This is a local marked period, not a sector trace or
a closed braid contribution.

The three complete directs are C for the actual complex packet,
E for the literal meridian matrix, and D for zero framing. They
are pinned below. No root-only asymptotic is differentiated to
define the meridian family.

## 1. Fixed marks and an exact parameter translation

Put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad
 M=e^\mu,\quad x=-M/q,
 \qquad x_0=-q^{-1}.
 \tag{1}
\]
The quantum parameter is fixed. Use C's four normalized finite
binomial packets with even widths, exact centers, and total-degree
sum. Their scaled center is
\[
 v_*=(\tau_*,\eta_*,\xi_*)\in
 K\Subset\{0<\xi<\eta<\tau<1\}.
\]
The widths have the protected support and uniform positive margins
specified in C. For an actual summation triple put
\(v=(T,a,c)/N\) and \(\Delta=v-v_*\).
Retain C's entropy \(R\), exact finite carrier phase
\(\vartheta_N\), and fixed mark
\[
 L_N=-\nabla R(v_*)-i\nabla\vartheta_N(v_*).
 \tag{2}
\]
In particular neither gradient in (2) is recomputed when \(M\)
varies. The packets, their normalization, and every centered
constant are fixed too. The variable tilt is \(z\in\mathbb C^3\).

Let \(X(M)=\kappa(M)S_2(M)D_{\rm red}(M)\) be the actual
opened positive generator. Define the finite period
\[
 \begin{split}
 P_N(\mu,z)=\sum_{T,a,c}&
 b_1(a)b_2(T-a)b_3(c)b_4(T-c)\,
 X(M)_{(c,T-c),(a,T-a)}\\
 &\hspace{8mm}\times e^{N(L_N+z)\cdot\Delta}.
 \end{split}                                                   \tag{3}
\]
All indices and packet caps are exactly C's. At \(\mu=0\),
this is C(7). The output is the prescribed algebraic row;
no conjugation of \(\mu\) or \(z\) is introduced.

E(2) gives the whole-meridian identity
\[
 \kappa(M)^{-1}X(M)_{c,a}
   =M^{c-3a}\kappa(1)^{-1}X(1)_{c,a}.
 \tag{4}
\]
Indeed the unique transfer \(a-c\) contributes
\(M^{-(a-c)}\), and the input diagonal contributes \(M^{-2a}\).
This holds on every degree block \(0\le T\le d\) used here,
including its endpoints; within those blocks both sides vanish
unless \(0\le c\le a\le T\).

Set
\[
 b=(0,-3,1),\qquad \theta_*=b\cdot v_*=\xi_*-3\eta_*.
\]
Since \(c-3a=N\theta_*+Nb\cdot\Delta\), substitution into
the finite sum proves exactly
\[
 \boxed{
 P_N(\mu,z)=\frac{\kappa(e^\mu)}{\kappa(1)}
       e^{N\mu\theta_*}P_N(0,z+\mu b).}
 \tag{5}
\]
There is no reindexing, interpolation in an occupation, or
discarded cap in (5). The shift changes only the displayed tilt.
The original meridian scalar remains explicit.

It is useful to keep two specified scalar conventions:
\[
 \overline P_N(\mu,z)=\kappa(e^\mu)^{-1}P_N(\mu,z),
 \qquad
 \widehat P_N(\mu,z)=x^d\overline P_N(\mu,z).
 \tag{6}
\]
The first removes only the common Cartan scalar. The second is
the period of the actual zero-framed generator
\(x^dS_2D_{\rm red}\): D(2) proves
\(\vartheta^{-1}X=x^dS_2D_{\rm red}\), with
\(\vartheta=\kappa x^{-d}\). Thus (6) distributes precisely
the original zero-framing line. In particular
\[
 \overline P_N(\mu,z)=e^{N\mu\theta_*}
                    \overline P_N(0,z+\mu b),\qquad
 \widehat P_N(\mu,z)=e^{d\mu+N\mu\theta_*}
                    \widehat P_N(0,z+\mu b).
 \tag{7}
\]

## 2. A fixed complex neighborhood and its actual saddle

Use C's critical point \(v_z\), critical value \(\Phi_*(z)\),
and its nonzero coefficient
\[
 A_N(z)=\frac{(2\pi)^{3/2}a(v_z)}{\sqrt{\det H_z}}.
 \tag{8}
\]
The notation retains the exact \(N\)-dependent centers and widths.
The square root is C's oriented Gaussian branch, obtained from
the positive real Gaussian and continued holomorphically.
On a fixed buffered tilt polydisk, C proves that \(A_N\), its
inverse, and every fixed derivative are uniformly bounded.
It also supplies a holomorphic relative error \(E_N(z)\), with
every fixed derivative \(O(N^{-1})\) on smaller polydisks.

Choose a fixed product polydisk in \((\mu,z)\), with a larger
buffered product polydisk, such that
\(w=z+\mu b\) stays in C's buffered domain. Its radii are
independent of \(N\). Define
\[
 \Psi(\mu,z)=\mu\theta_*+\Phi_*(w),\qquad
 \widehat\Psi(\mu,z)=\mu(1+\theta_*)+\Phi_*(w).
 \tag{9}
\]
Equations (5)--(8) and C's actual period theorem give
\[
 \boxed{\begin{split}
 \overline P_N(\mu,z)
 &=e^{iN\vartheta_N(v_*)}e^{N\Psi(\mu,z)}
                       A_N(w)(1+E_N(w)),\\
 \widehat P_N(\mu,z)
 &=x_0^d e^{iN\vartheta_N(v_*)}e^{N\widehat\Psi(\mu,z)}
                    e^{-\mu}A_N(w)(1+E_N(w)).
 \end{split}}                                                \tag{10}
\]
The factor \(e^{-\mu}\) is the exact endpoint correction
\(d=N-1\), not an unrecorded change of phase. Both leading
coefficients are units. For all large \(N\), both actual periods
are nonzero on the smaller product polydisk.

The complete remainder in (10) is literally \(E_N(z+\mu b)\).
Hence every fixed mixed \(\mu,z\) derivative of that normalized
relative remainder is \(O(N^{-1})\). This proves a genuine
fixed-size meridian-family statement; it is stronger than
continuity of the root value or a pointwise real asymptotic.

The cycle and its coefficient have also been retained. For each
\(w=z+\mu b\), C derives its period from the original threefold
finite cotangent rectangles, all seven mixed side remainders,
and the independent physical cap complement. It then deforms the
main boxed integral to the translated critical point \(v_w\),
with coefficient \(+1\). Our change is the exact equality (5),
so the same contours and bounds apply at \(w\). The additional
factor \(e^{N\mu\theta_*}\) multiplies the main term and every
remainder alike. It does not change a relative gap. The
meridian-dependent deformation is precisely C's deformation at
\(w\); no additional contour choice or packet normalization is
introduced.

The actual critical occupations are \(v_w\). In particular the
clock insertions of C remain literal finite insertions and give
\[
 \frac{P_N[K_{\rm tot}(M);\mu,z]}{P_N(\mu,z)}
       =x(M)^2e^{-2\pi i\tau_w}(1+O(N^{-1})),
 \tag{11}
\]
with the corresponding \(x(M)e^{-2\pi i\ell_i v_w}\) for
individual input or output heads. Their normalized remainders
have all fixed mixed derivatives on smaller domains. Thus fixed
nonreal clock values are compatible with the actual meridian
family of this local period, without changing a physical index.

## 3. True normals, including zero framing

Critical-value differentiation in C gives
\(\nabla_z\Phi_*(w)=v_w-v_*\). Therefore
\[
 \partial_\mu\Psi=\theta(w):=\xi_w-3\eta_w,
 \qquad
 \partial_\mu\widehat\Psi=r(w):=1+\xi_w-3\eta_w.
 \tag{12}
\]
Differentiating the proved holomorphic expansion, rather than an
isolated root formula, gives
\[
 \begin{split}
 \partial_\mu\log\overline P_N
 &=N\theta(w)+b\cdot\nabla\log A_N(w)+O(N^{-1}),\\
 \partial_\mu\log\widehat P_N
 &=Nr(w)-1+b\cdot\nabla\log A_N(w)+O(N^{-1}).
 \end{split}                                                \tag{13}
\]
The logarithmic derivatives do not depend on choosing a scalar
logarithm of the nonzero period. All fixed mixed derivatives of
the displayed remainders obey the same bound.

On the real center, \(\theta(0)=\xi_*-3\eta_*<0\), uniformly
away from zero on \(K\). After shrinking the parameter domain,
the scalar-normalized first normal is consequently nonzero, with
\[
 \frac{\partial_\mu\overline P_N}{\overline P_N}
                   =N\theta(w)+O(1).
 \tag{14}
\]
For the actual zero-framed generator the explicit additional
condition is
\[
                         |1+\xi_w-3\eta_w|\ge r_0>0.
 \tag{15}
\]
This is a nonempty open condition, for example by choosing protected
centers off the proper plane \(1+\xi_*-3\eta_*=0\) and shrinking
their neighborhood. It is not asserted on every allowed center.
On compact subcharts satisfying (15),
\[
 \frac{\partial_\mu\widehat P_N}{\widehat P_N}
                     =Nr(w)+O(1)
\]
is nonzero for all large \(N\). More generally, for fixed \(j\ge1\),
\[
 \frac{\partial_\mu^j\overline P_N}{\overline P_N}
       =N^j\theta(w)^j+O(N^{j-1}),\qquad
 \frac{\partial_\mu^j\widehat P_N}{\widehat P_N}
       =N^jr(w)^j+O(N^{j-1}).                         \tag{16}
\]
These are additive estimates even where a leading power vanishes.
They follow directly from (10): derivatives hitting a phase factor
give the leading powers, and all other product-rule terms have
at most \(j-1\) factors of \(N\).

For clarity, on the scaled collar \(\mu=u/N\), uniformly for
bounded complex \(u\) and smaller fixed \(z\)-domains,
\[
 \frac{\overline P_N(u/N,z)}{\overline P_N(0,z)}
       =e^{u\theta(z)}(1+O(N^{-1})),\qquad
 \frac{\widehat P_N(u/N,z)}{\widehat P_N(0,z)}
       =e^{ur(z)}(1+O(N^{-1})).                       \tag{17}
\]
All fixed \(u,z\) derivatives of these normalized remainders are
\(O(N^{-1})\), by Taylor expansion of (10) on its buffered domain
and Cauchy estimates. Keeping \(d/N+\theta(z)\) instead of \(r(z)\)
in the second exponential is equally valid and records the exact
linear endpoint term. No \(u\)-dependent power of \(N\) is hidden
in (17): the amplitude in (10) is the explicitly bounded unit
\(e^{-\mu}A_N(z+\mu b)\).

For the unnormalized generator the full scalar restoration is
\[
 \partial_\mu^jP_N(\mu,z)
 =\sum_{i=0}^j\binom ji
   \partial_\mu^i\kappa(e^\mu)\,
   \partial_\mu^{j-i}\overline P_N(\mu,z).
 \tag{18}
\]
In particular its logarithmic derivative contains
\(\partial_\mu\log\kappa(e^\mu)\) in addition to the first
line of (13). No formula or growth assumption for an omitted
Cartan derivative is used. All zero-framed derivatives, by
contrast, are already explicit in (10)--(17).

## 4. Fixed annuli and the remaining source interfaces

Keep C's original input and output coherent annular matrices
\(W_{\rm in},W_{\rm out}\). Their fixed margins contain the
entire corresponding packet supports. Their entries do not
depend on \(\mu\) or \(z\). Define the two finite current periods
by replacing \(X\) in (3) with
\[
 W_{\rm out}X(M)-X(M)W_{\rm in},\qquad
 W_{\rm out}X(M)W_{\rm in}-X(M).
 \tag{19}
\]
These windows are diagonal, so each entry in (19) has exactly the
same meridian factor (4). Equation (5) therefore holds for each
current as well. C(25) gives, on our buffered parameter domain,
\[
 |J_{N,1}(\mu,z)|+|J_{N,2}(\mu,z)|
                  \le Ce^{-cN}|P_N(\mu,z)|.           \tag{20}
\]
The same statement holds in the scalar-normalized and zero-framed
conventions, since their scalar factors are identical on the
period and its currents.

The ratios \(J_{N,i}/P_N\) are holomorphic there: after cancelling
the common scalar they divide the nonzero function in (10).
Cauchy estimates prove an \(O(e^{-cN})\) bound for every fixed
mixed derivative of these ratios on a smaller domain. In
particular, writing \(\mathcal D\) for a mixed derivative of
total order \(s\), for either explicit convention (6),
\[
       |\mathcal D J_{N,i}|\le
          C_sN^s e^{-cN}|P_N|.                       \tag{21}
\]
Here the period and current on both sides use that same convention.
The estimate follows by the product rule and
\(|\mathcal D P_N|\le C_sN^s|P_N|\), itself a consequence of
(10). It is not differentiation of an absolute-value inequality.
On (15), the first zero-framed current derivative is therefore
exponentially small relative to the nonzero first normal.
Raw Cartan factors and derivatives are restored by (18) for the
currents too. If a window or frame were moved with \(M\), its
own derivative would be an additional term, absent here because
the marks were fixed in (2)--(3),(19).

This pays the differentiated local period hypothesis for this
specific opened generator and these supplied packets. The slope
in (12) is its local marked occupation symbol; it is not asserted
to be the longitude of a closed braid. No claim is made that
this packet-marked meridian family satisfies a complementary Gauss
range condition, equals a prescribed exterior row, composes around
a word, or isolates an actual geometric trace sector. In particular
(15) does not establish noncancellation in the original closing
functional. Quantum-parameter derivatives are outside the theorem.

## Complete proof directs

* C: notes/research_opened_generator_complex_clock_packet.md,
  486 lines, SHA256
  b14feee0a1ae26d69c8cd13945ed02b4492847da022d3ae1e7a41199892d46be.
* E: notes/research_opened_generator_meridian_collar_transport.md,
  240 lines, SHA256
  2cf2984b95230b61ee41f4c9ae3e0cf727b54e967727d7468f45242a532266f7.
* D: notes/research_marked_reduced_action_meridian_parity.md,
  452 lines, SHA256
  df919e67b960783888ba98d455813c1cff2c0aeb04ac14533821d6cff6b9b21d.

Only written mathematics and text/hash operations are used. All
three complete directs were freshly read nontruncated in this
author sequence. The entire matching final was freshly read back,
every used implication checked, and all four hashes renewed before
author freeze. Independent matching peer and root review remain
separate. Frozen and public files are unchanged.
