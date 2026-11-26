# A strict loss for the original radical observation

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The bounded physical weights of a high Newton insertion give more
than a supremum estimate when its spectator is an original source
with whole-boundary decay. Near the last physical row the weights
alternate. The exact crossing values are a Gaussian chirp, so a
cosecant contour retains that cancellation and gives a strict
exponential loss. This holds uniformly over the entire radical,
at both parities and for every fixed signed crossing power.

The result improves the radical-matching step in an induction on
path length. It does not estimate the remaining joint low-sector
cycle or assert a new lower bound for that cycle.

## 1. The source and the estimate

Use the original physical algebra, trace, crossing and Newton
polynomials from [the radical contraction proof](research_high_newton_radical_contraction.md).
Put
\[
 D=N-1,\qquad m=\lfloor N/2\rfloor,\qquad
 c_a=2\cos((2a+1)\pi/N),\qquad
 \mathcal R_{n,r,N}f=\phi_N(R^n e_{D-r}f),\quad 0\le r<m.
 \tag{1}
\]
Here \(n\) is any fixed integer, including zero. The spectator
\(f_N(w)\) is its literal ordinary polynomial, not a representative
chosen after reducing a free boundary variable. Its degree is not
required to be less than \(N\).

Assume that for some fixed \(c>0,B\ge0,h_0>0\),
\[
 |f_N(-2\cos(t+ih))|
 \le C N^A\exp\{N[M-c(1-\cos t)+Bh^2]\},
       \quad -\pi\le t\le\pi,\quad |h|\le h_0.
 \tag{2}
\]
These are the actual whole-period and quadratic-strip bounds
proved for the sources in
[the boundary-decay theorem](research_network_whole_boundary_decay.md).
The following argument also allows spectator parameters, provided
(2) holds uniformly in them. In particular it applies to every
fixed ordinary derivative in uncontracted boundary variables.

**Theorem 1.** Under (2), there are \(\delta>0\), \(C',A'\)
such that, uniformly for every \(0\le r<m\),
\[
                 |\mathcal R_{n,r,N}f_N|
                      \le C'N^{A'}e^{N(M-\delta)}.
 \tag{3}
\]
The constants depend on the fixed \(n,c,B,h_0\), not on \(r\)
or \(N\). Both level parities and all original physical normals
are included. No assertion that (3) is the sharp rate is made.

One explicit positive choice is obtained from
\[
 \begin{split}
 T_0&=\min\{1/2,\ \pi/[2(1+|n|)]\},\\
 h&=\min\{h_0/2,\ 1/4,\ 1/[16(1+B)]\},\\
 d_0&=c(1-\cos(T_0/2)),\qquad \epsilon=1/16,\\
 \delta&=\min\{c(1-\cos(\pi/8)),\ h/8,\ d_0/2\}.
 \end{split}
 \tag{4}
\]
Only sufficiently large levels are needed for these particular
constants. Finitely many smaller levels may be absorbed in \(C'\)
whenever the input family is defined there.

## 2. Exact full-node and alternating formulas

The original radical identity is
\[
 \mathcal R_{n,r,N}f_N
   =(-1)^rS_r^2\sum_{a=0}^r
       \frac{R(c_a)^n f_N(c_a)}
            {\prod_{0\le b\le r,\ b\ne a}(c_a-c_b)}.
 \tag{5}
\]
It is an identity for the full trace. At a double node, the
radical's value is zero, so its derivative consumes the original
normal and only the spectator's value remains. At odd levels the
radical also vanishes at the simple node \(-2\). Thus (5) has
not discarded a spectator normal.

Let \(Q_N\) be the monic polynomial of the double nodes only,
and put
\[
 \begin{split}
 Q_N(w)&=\prod_{a=0}^{m-1}(w-c_a)
   =\begin{cases}2T_m(w/2),&N=2m,\\
                 U_m(w/2)-U_{m-1}(w/2),&N=2m+1,
     \end{cases}\\
 D_r(w)&=\prod_{a=r+1}^{m-1}(w-c_a),\qquad
                             \ell=m-1-r.
 \end{split}
 \tag{6}
\]
The odd simple node is deliberately absent from \(Q_N\).
Multiplication by the missing-node factor gives exactly
\[
 \mathcal R_{n,r,N}f_N
   =(-1)^r S_r^2\sum_{a=0}^{m-1}
          \frac{D_r(c_a)R(c_a)^n f_N(c_a)}{Q_N'(c_a)}.
 \tag{7}
\]
There are no derivatives of \(D_r\) in this value formula.
The added terms vanish at their literal missing nodes.

Write \(t_a=\pi-(2a+1)\pi/N\), so \(c_a=-2\cos t_a\).
The elementary trigonometric derivatives of (6) give
\[
 \frac1{Q_N'(c_a)}=
 \begin{cases}
  \displaystyle\frac2N(-1)^a\sin t_a,&N=2m,\\[1mm]
  \displaystyle\frac4N(-1)^a\sin t_a\sin(t_a/2),&N=2m+1.
 \end{cases}
 \tag{8}
\]
The exact original crossing values are
\[
 R(c_a)^n=C_{N,n}\exp\left(\frac{inNt_a^2}{4\pi}\right),
       \qquad C_{N,n}=\exp\left(\frac{\pi i n(N-1)^2}{4N}\right).
 \tag{9}
\]
Only after the original radical contraction has reduced the trace
to values do we use this entire Gaussian representative. No claim
is made that its off-grid derivative equals the crossing normal.

For clarity, the exact symmetric alternating sums are as follows.
Define
\[
 \begin{split}
 G_e(t)&=\sin t\ D_r(-2\cos t)f_N(-2\cos t)
                          e^{inNt^2/(4\pi)},\\
 G_o(t)&=\sin t\sin(t/2)D_r(-2\cos t)f_N(-2\cos t)
                          e^{inNt^2/(4\pi)}.
 \end{split}
 \tag{10}
\]
Then
\[
 \mathcal R_{n,r,N}f_N=
 \begin{cases}
 \displaystyle\frac{(-1)^{r+m-1}C_{N,n}S_r^2}{N}
       \sum_{k=-m}^{m-1}(-1)^k G_e((2k+1)\pi/N),&N=2m,\\[2mm]
 \displaystyle\frac{2(-1)^{r+m}C_{N,n}S_r^2}{N}
       \sum_{k=-m}^{m}(-1)^k G_o(2k\pi/N),&N=2m+1.
 \end{cases}
 \tag{11}
\]
For even levels the summand is invariant under \(k\mapsto-k-1\).
For odd levels it is invariant under \(k\mapsto-k\), and
the added term at zero vanishes because \(G_o(0)=0\).
This is exactly how the absent odd simple-node contribution is
retained; it is not replaced by a double-node normal.

There is a useful elementary bound
\[
                         S_r^2\le N\quad(0\le r<m).
 \tag{12}
\]
The factors \(2\sin(j\pi/N)\), for \(j<N/2\), cross one
only once, so their successive products first decrease and then
increase. At odd levels \(S_m^2=N\); at even levels
\(S_{m-1}^2=N/2\), by the full sine product and reflection.
These endpoint values and \(S_0=1\) prove (12).

## 3. Proof of the strict loss

First suppose \(\ell\ge\epsilon N\). In the bounded-weight
version of (5), every sampled node satisfies
\(t_a\ge2\pi\epsilon\). Each weight has magnitude at most
two, by the radical contraction theorem. The original crossing
values have modulus one. Equation (2) on the real line therefore
gives (3) with loss \(c(1-\cos(2\pi\epsilon))\).

It remains to consider \(\ell<\epsilon N\), using (11).
Every missing node has angle at most \(2\pi\ell/N<\pi/8\).
On the central rectangle \(|\Re t|\le T_0\le1/2\),
\(|\Im t|\le h\le1/4\), we have \(|t|<3/5\), so
each missing-node factor satisfies
\[
 \begin{split}
 |-2\cos t-c_a|
 &\le2(\cosh(3/5)-1)+(\pi/8)^2<3/5,\\
 |D_r(-2\cos t)|&\le(3/5)^\ell\le1.
 \end{split}
 \tag{13}
\]
For the numerical constant, the positive cosh series gives
\(\cosh(3/5)\le1+(9/50)/(1-3/100)<6/5\), and
\(\pi<22/7\) completes the rational comparison.
The sine factors in (10) are uniformly bounded on this strip.

Choose a positive physical midpoint \(T_N\le T_0\) such that
\(T_N\to T_0\), with both \(\pm T_N\) midway between
adjacent sampling nodes. Eventually \(T_N\ge T_0/2\).
The terms with \(|t_k|\ge T_N\) are bounded directly in
(5), using the original weights of magnitude at most two.
The full-node and symmetric formulas add only zero terms or
the equal reflected copies. Hence this outer part has rate at
most \(M-d_0\), with no cost for \(D_r\). Only the central
part uses the estimate (13).

For the remaining alternating sum put \(t_0=\pi/N\) at
even levels and \(t_0=0\) at odd levels. On the counterclockwise
rectangle \(\mathcal Q_N=[-T_N,T_N]+i[-h,h]\), the exact
residue identity is
\[
 \sum_{t_k\in(-T_N,T_N)}(-1)^kG(t_k)
       =\frac{N}{4\pi i}\oint_{\partial\mathcal Q_N}
          \frac{G(t)}{\sin\{N(t-t_0)/2\}}\,dt.
 \tag{14}
\]
The function \(G\) is entire, and the residues of the reciprocal
sine are \(2(-1)^k/N\). No periodicity of the Gaussian in
(10) is needed. The four sides and all the poles inside are kept.

On a horizontal side the reciprocal sine is at most
\(C e^{-Nh/2}\). For \(|\Re t|\le T_N\), the Gaussian
in (10) costs at most \(e^{Nh/4}\), since
\(|n|T_0/(2\pi)<1/4\). By (2), (4), and (13), the rate
on these sides is at most
\[
                 M+Bh^2-h/4\le M-3h/16<M-h/8.
 \tag{15}
\]
Here \(Bh\le1/16\), and (13) contributes no positive exponent.
At either vertical side, the midpoint choice gives the exact
denominator modulus \(\cosh(Ny/2)\), hence inverse modulus
at most \(2e^{-N|y|/2}\). The crossing cost is at most
\(e^{N|y|/4}\), while \(By^2\le|y|/16\).
The real angle stays at \(\pm T_N\), with its loss \(d_0\).
Therefore every vertical point, including \(y=0\), has rate
\[
                 \le M-d_0-3|y|/16
                            <M-d_0/2.
 \tag{16}
\]
Thus no zero-height endpoint current is omitted. Equations
(11)--(16), the polynomial bound (12), and the number of sampled
nodes prove (3) with (4).

All estimates are uniform in any retained spectator parameters.
Differentiation in those ordinary variables commutes with the
finite trace and sums. Apply the same proof to the differentiated
spectator, using its version of (2). This proves the stated normal
and parameter assertions. \(\square\)

## 4. Consequence for whole radical matchings

Consider the original path contraction and a nonempty matching
\(\mathfrak m\) of selected--selected radical edges. Delete those
edges, evaluate their endpoints, and let \(F_{C,N}\) be the
remaining original component sources, as in
[the exact path matching formula](research_radical_path_sector_gap.md#1-what-remains-after-a-radical-matching-is-contracted).
Every untouched edge stays present, including a bare edge between
two evaluated vertices. Suppose these smaller component sources
have their proved separated multivariable bounds
\[
 |\partial_{\mathbf z}^{\alpha}
        F_{C,N}(-2\cos(\mathbf t+i\mathbf h))|
 \le C_\alpha N^{A_\alpha}
   \exp N\left[M_C-\sum_{b\in\partial C}
                   c_{Cb}(1-\cos t_b)
                     +\sum_{b\in\partial C}B_{Cb}h_b^2\right],
\]
uniformly on a fixed product strip, where every \(c_{Cb}>0\).
The sums here, rather than separate unrelated one-variable bounds,
are needed for iteration. The existing whole-boundary source
theorems supply exactly this form, including every required fixed
ordinary boundary derivative.

Before summing the radical labels, the matching term is exactly
\[
 \mathscr T_{\mathfrak m,N}
  =\sum_{0\le r_e<m\ (e\in\mathfrak m)}
     \left(\prod_{v\in V(\mathfrak m)}
             \mathcal R_{n_v,r_{e(v)},N}^{(z_v)}\right)
                  \prod_C F_{C,N}(\mathbf z_{\partial C}).
 \tag{17}
\]
Each removed vertex belongs to exactly one matching edge.
At a degree-two vertex its remaining incidence is a boundary
variable of one component. Apply Theorem 1 in that variable.
After this operation the spectator is still an ordinary polynomial
in every other boundary variable, with the same separated angular
loss and strip bound there, so the operations may be iterated.
At a degree-one removed vertex no remaining factor depends on
its color; use the original polynomial bound
\(|\mathcal R_{n,r,N}1|\le2m\) instead.

Consequently, for some fixed \(\delta_v>0\),
\[
 |\mathscr T_{\mathfrak m,N}|
 \le C N^A\exp N\left[
       \sum_C M_C-
        \sum_{\substack{v\in V(\mathfrak m)\\d_v=2}}\delta_v
                           \right].
 \tag{18}
\]
The sum over the at most \(m^{|\mathfrak m|}\) radical labels
is polynomial at fixed path length. All original outside-period
losses, sufficiently thin quadratic strips, and their ordinary
derivatives survive in (18). A bare-edge component has the same
boundary bounds by the full edge estimates and their Laurent
continuation; it is not assigned polynomial size.

For comparison, the earlier matching estimate gave only rate
\(\sum_C M_C\). Formula (18) proves a further strict loss from
the actual alternating observation. It is an upper bound for the
complete coherent radical terms, not a positive-Gram replacement
of them. The exact action identity remains
\(\sum_C M_C=M_\Gamma(\chi^{V(\mathfrak m)})-
|\mathfrak m|M_\infty\). Comparing that quantity with the
desired unit-charge action, and controlling the remaining joint
low-sector cycle, are separate tasks. No universal activation
inequality or nonzero low-cycle coefficient is inferred here.

## 5. The original midpoint insertion

The same loss holds for the adjacent low insertion that occurs in
the exact cutoff current. Put \(L=D-m\) and define
\[
 \mathcal E_{n,N}f=\phi_N(R^n e_Lf).
 \tag{19}
\]
By the original Newton trace pairing this is the coefficient of
\(e_m\) in \(R^nf\) in the full physical quotient. Thus it is
the literal midpoint observation of
[the cutoff-current identity](research_bare_kernel_power_three_obstruction.md#6-the-midpoint-forcing-after-the-original-internal-pair-trace).

**Theorem 2.** Under (2), at both parities,
\[
                  |\mathcal E_{n,N}f_N|
                     \le C'N^{A'}e^{N(M-\delta)}
 \tag{20}
\]
with the same choice (4), after enlarging the polynomial constant.
The spectator and crossing first normals at the even repeated node,
and the odd simple endpoint, are retained.

Here are the exact formulas and the endpoint checks. For odd
\(N=2m+1\), the first \(m+1\) Newton nodes are distinct and
include \(-2\). Their monic polynomial is
\((w+2)Q_N(w)\), and \(S_m^2=N\). Newton interpolation,
followed by the two angular preimages of every double physical
node, gives
\[
 \mathcal E_{n,N}f_N=C_{N,n}\sum_{k=-m}^{m}(-1)^k
  \cos(t_k/2)f_N(-2\cos t_k)e^{inNt_k^2/(4\pi)},
                  \qquad t_k=2\pi k/N.
 \tag{21}
\]
The term \(k=0\) is present. Its coefficient is exactly
\(C_{N,n}=R(-2)^n\), so it is the original simple-node term,
not a spurious extra angular residue. The cosecant identity (14)
applies with \(G(t)=\cos(t/2)f_N(-2\cos t)e^{inNt^2/(4\pi)}\).
The bounded cosine replaces the bounded factors (10), and no
missing-node product is needed. The outer real terms have bounded
weights and loss \(d_0\). Equations (15)--(16) prove (20).

For even \(N=2m\), the coefficient \(e_m\) repeats the last
node \(c_*=c_{m-1}=-2\cos(\pi/N)\). Write \(g=R^nf_N\),
with its actual physical values and first normals. The confluent
divided difference is exactly
\[
 \begin{split}
 \mathcal E_{n,N}f_N=(-1)^m S_m^2\bigg[&
    \sum_{a=0}^{m-2}\frac{g(c_a)}{(c_a-c_*)Q_N'(c_a)}\\
   &+\frac{g'(c_*)-g(c_*)
          \sum_{a=0}^{m-2}(c_*-c_a)^{-1}}{Q_N'(c_*)}
                                    \bigg],\qquad S_m^2=2N.
 \end{split}
 \tag{22}
\]
The first-normal identity needed to pull this formula back to
angles is the exact original one
\[
 \frac{(R^n)'(c_a)}{R(c_a)^n}
       =\frac{inNt_a}{4\pi\sin t_a}.
 \tag{23}
\]
Consequently the Gaussian representative (9) matches both jets
at the repeated node. On any symmetric angular rectangle that
encloses the desired physical nodes, the corresponding part of
(22) is
\[
 \frac{NC_{N,n}}{2\pi i}\oint
  \frac{\sin t\, f_N(-2\cos t)e^{inNt^2/(4\pi)}}
       {(-2\cos t-c_*)\cos(Nt/2)}\,dt.
 \tag{24}
\]
Each positive physical angle has its negative preimage. Their
equal residues supply the factor two in \(S_m^2=2N\).
The poles at \(\pm\pi/N\) are double and recover the entire
second line of (22); they are not removed from (24).

Use the central midpoint rectangle of §3. Eventually both double
poles lie inside it. On its horizontal sides,
\(|-2\cos t-c_*|\ge4\sinh^2(h/2)\); on the vertical
sides it is at least \(4\sin^2(T_0/8)\). These follow by
factoring \(-2\cos t+2\cos(\pi/N)\) into the two sine
factors at \((t\pm\pi/N)/2\), and using
\(T_N\ge T_0/2\), \(\pi/N\le T_0/4\).
Thus the extra denominator costs a fixed constant on the contour.
The reciprocal cosine has exactly the same horizontal decay and
midpoint vertical bound as the reciprocal sine in (14). All the
central estimates (15)--(16) still apply. The omitted real nodes
in (22) have coefficients bounded by a power of \(N\): use
\(|Q_N'(c_a)|^{-1}\le2/N\) and the minimum distinct-node
spacing bounded below by a positive constant times \(N^{-2}\).
The sole first-normal term remains inside the central contour.
Their angular loss is \(d_0\), proving (20). Uniform spectator
parameters and ordinary derivatives follow exactly as in Theorem 1.
\(\square\)

For a cutoff edge with two distinct selected endpoints, one
endpoint receives (19) and the other a radical insertion. If their
remaining component factors satisfy the separated bound in §4,
Theorems 1 and 2 give the two corresponding strict losses before
an absolute estimate of the cutoff forcing. This statement does
not assign one loss per factor to overlapping cutoff edges at the
same vertex, where products of insertions must first be treated
in the original algebra. It also does not supply the missing
coefficient of the joint low-sector cycle.

## 6. Reproduction

The [focused checker](../experiments/check_radical_observation_boundary_decay.py)
constructs the original crossing by polynomial multiplication in
the full Newton quotient. It compares the literal trace, including
its ordinary top-coefficient normalization, with (7) and (11) at
both parities and signed powers, using also a spectator of degree
greater than \(N\). It also checks (21)--(23) against the literal
midpoint trace, including its repeated-node normal, and checks
the scalar contour reserves exactly.
Its [record](../repro/results/research-radical-observation-boundary-decay.json)
is a normalization check; the uniform loss is the written contour
proof above, not an inference from finite numerical data.
