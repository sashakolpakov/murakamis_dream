# Paying the taller low horizontal by complete Newton row norms

Private written finite-source deduction, 9 November 2026. The exact
Cauchy--Schwarz inequality for the two shortened kernels pays the
first-angle segment from \(2\pi/3-i/10\) to \(5\pi/6-i/10\).
The outgoing domain is the whole independent lower rectangle of
height \(7/10\). Every shortened Newton row is retained, including
the rows beyond the real numerator zero. No coherent edge packet
on this low segment is assumed.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, or frozen-source edit is used.

## 1. Original source and statement

Keep the calibrated cubic and action from the
[taller strip theorem](research_mixed_symmetric_closing_strip_phase_and_tail.md):
\[
 u=\beta-iK,\qquad 0\le\beta\le\pi/2,\quad0\le K\le7/10,
 \qquad s(u)=\Re S_3(0,u).
 \tag{1}
\]
The notation for the actual ordinary source is
\[
 \begin{gathered}
 D=N-1,\quad U=\lfloor N/2\rfloor-1,\quad
 c_\nu=2\cos((2\nu+1)\pi/N),\\
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(X)=S_j^{-2}\prod_{\nu<j}(c_\nu-X),\\
 K_N^<(t,u)=\sum_{j=0}^{U}e_j(-2\cos t)e_j(-2\cos u),\\
 g_N^{<<}(t,u)=\sin t\,K_N^<(t,0)K_N^<(t,u)
                                     e^{3iNt^2/(4\pi)},\\
 \eta_N=(-1)^{N-1},\quad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\quad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
 \end{gathered}
 \tag{2}
\]
These are the same full multiplier and normalization as in the
[one-remaining-current identity](research_mixed_next_inner_three_single_remaining_current.md).
Put \(h_0=1/10\), \(a_0=2\pi/3\), \(a_1=5\pi/6\), and orient
\[
 \gamma_L:\quad a_0-ih_0\longrightarrow a_1-ih_0 .
 \tag{3}
\]

**Theorem.** Uniformly on (1), at both parities and all sufficiently
large \(N\),
\[
 \frac{N^2}{\pi}\int_{\gamma_L}
          |g_N^{<<}(t,u)W_N(t)|\,|dt|
             \le C e^{N(s(u)-1/100)}.
 \tag{4}
\]
In particular this bounds the original signed current with factor
\(-N^2C_{N,3}/(\pi i)\). It joins the paid
[diagonal taper](research_mixed_symmetric_closing_diagonal_taper.md)
to \(5\pi/6-i/10\). The far part beyond that endpoint, the earlier
trace deletions, and the outer ordinary closing are separate
source obligations.

## 2. The complete diagonal row profile

For \(z=a-ih\), with real \(a,h\), set
\[
 J(y)=\int_0^y\log(2\sin\pi x)\,dx,\qquad
 V_z(y)=\int_0^y
       \log|2\cos(2\pi x)+2\cos z|\,dx-2J(y),
 \quad0\le y\le1/2,
\]
\[
 m(a,h)=\max_{0\le y\le1/2}V_{a-ih}(y).
 \tag{5}
\]
The midpoint product estimate in
[the real Newton theorem, Lemma 1](research_three_crossing_real_period_newton_bound.md)
and its compact-height version in
[the complete far-angle theorem, Section 2](research_mixed_next_outer_far_angles_and_verticals.md)
give, on every fixed bounded angular-height rectangle,
\[
 |e_j(-2\cos z)|\le C N^A e^{NV_z(j/N)}
                         \qquad(0\le j\le U).
 \tag{6}
\]
The larger fixed height \(7/10\) changes only the compact constant
in this mesh proof. Indeed the two numerator factors are the
shifted cosines
\[
 4\cos(\pi(\nu+1/2)/N+z/2)
       \cos(\pi(\nu+1/2)/N-z/2).
 \tag{7}
\]
Away from their bounded number of possible zero cells the
logarithmic derivative is bounded by a constant times inverse
distance to the zero, yielding an \(O(\log N)\) sum. On a zero
cell the one-sided sampled logarithm minus its integral average
is uniformly bounded; a literal zero only improves the upper
bound. The denominator has the uniform original sine-factorial
estimate. This argument is uniform as \(h\) tends to zero and
as \(j/N\) tends to either endpoint. It estimates the entire
initial product, not just its part before a numerator zero.

Consequently the exact, finite Cauchy--Schwarz inequality gives
\[
 \begin{split}
 |K_N^<(t,u)|
 &\le
 \left(\sum_{j=0}^{U}|e_j(-2\cos t)|^2\right)^{1/2}
 \left(\sum_{j=0}^{U}|e_j(-2\cos u)|^2\right)^{1/2}\\
 &\le C N^A
          e^{N\{m(\Re t,-\Im t)+m(\beta,K)\}} .
 \end{split}
 \tag{8}
\]
There is no positivity assertion about the original signed kernel.

Here are the needed exact properties of (5). Write
\[
 p=\cos a,\quad q=\cosh h,\quad v=(q-p)/2.
 \tag{9}
\]
Whenever \(1+pq>0\) and \(0\le v<1\), the maximum is unique
and interior, with
\[
 \cos(2\pi y_*)=\frac{1-|\cos(a-ih)|^2}{2(1+pq)}.
 \tag{10}
\]
To verify this, put \(x=\cos(2\pi y)\). The sign of
\(\partial_yV\) is the sign of
\[
 |x+\cos(a-ih)|^2-(1-x)^2
       =2(1+pq)x+|\cos(a-ih)|^2-1.
 \tag{11}
\]
At \(x=1\) it is positive; at \(x=-1\) it is negative
because \(|\cos(a-ih)-1|/2=v<1\). Thus the force crosses
one exactly once. This includes all the rows after the
real zero, where the logarithm in (5) can be singular.

For every \(h\ge0\) and \(0<a<\pi\), independently of (10),
\[
 \partial_a V_{a-ih}(y)
  =\frac1{2\pi}
       \log\left|
        \frac{\cos(\pi y+(a-ih)/2)}
             {\cos(\pi y-(a-ih)/2)}\right|\le0
                  \qquad(0\le y\le1/2).
 \tag{12}
\]
For example the squared modulus in the numerator minus that
in the denominator is
\(-\sin(2\pi y)\sin a\). Endpoint values follow by continuity,
and real logarithmic singularities by their integrable limits.
It follows that \(m(a,h)\) is nonincreasing in \(a\).

On the domain of (10), a direct stationary differentiation gives
\[
 m_{hh}(a,h)=
 \frac{\Re(\overline c/c)+|\sin((a-ih)/2)|^2}
      {2\pi\sqrt{\,1-v^2\,}},
 \qquad c=\cos((a-ih)/2),
 \tag{13}
\]
and \(m_h(a,0)=0\). We give the branch justification, so that
this formula is not an appeal to a two-angle packet.
Choose the logarithm in the integral in (5) up to \(y_*\)
by continuation from \(h=0\). That initial segment is zero-free.
With \(\zeta=\tan(\pi y_*)\), (10) gives
\[
 \zeta=\frac{|c|^2}{\sqrt{1-v^2}}.
 \tag{14}
\]
The derivative of its holomorphic numerator primitive is
\[
 -\frac1\pi\operatorname{artanh}
       \{\tan((a-ih)/2)\zeta\}
 =-\frac1\pi r,\qquad
 \sinh r=\overline c\,\tan((a-ih)/2),\quad
 \cosh r=\frac{\sqrt{1-v^2}}{c}.
 \tag{15}
\]
At zero height this is the positive real return
\(r=\operatorname{arsinh}(\sin(a/2))\).
The last expression in (15) has positive real part and never
vanishes. It fixes the same continuous branch throughout
the domains used below. The real endpoint derivative vanishes
at the maximizing row, so \(m_h=-\Im r/\pi\). Differentiating
(15), with the conjugate angle moving in the opposite
direction, gives
\[
 r_h=-i\,\frac{\overline c/c+|\sin((a-ih)/2)|^2}
                        {2\sqrt{1-v^2}},
 \tag{16}
\]
which proves (13). These formulas also extend to \(a=0\) and
\(h=0\) by continuity.

Since
\[
 \Re(\overline c/c)=\frac{1+pq}{q+p}\le1,\qquad
 |\sin((a-ih)/2)|^2=v,
 \tag{17}
\]
equation (13) yields the useful upper bound
\[
 m_{hh}(a,h)\le\frac1{2\pi}
                     \sqrt{\frac{1+v}{1-v}}.
 \tag{18}
\]
Only domains with \(q+p>0\) are used in (17).

## 3. Uniform first and outgoing row bounds

The original real profile has
\[
 m(0,0)=b_2<7/12,\qquad
 m_a(a,0)=-\frac1\pi\operatorname{arsinh}(\sin(a/2)).
 \tag{19}
\]
In particular the real Newton theorem gives
\[
 m(\beta,0)\le b_2-\frac{1-\cos\beta}{2\pi}.
 \tag{20}
\]
At the first endpoint \(a_0=2\pi/3\), integrating
\(\operatorname{arsinh}x\ge x-x^3/6\) gives the sharper
bound
\[
 m(a_0,0)\le b_2-\frac{67}{72\pi}.
 \tag{21}
\]
Equivalently insert \(\cos(a_0/2)=1/2\) in equation (16)
of that real Newton theorem.

On the full outgoing rectangle (1), the positive-series bound
\[
 \cosh(7/10)
 \le1+\frac{49}{200}
       +\frac{2401/240000}{1-49/3000}
 <\frac{13}{10}
 \tag{22}
\]
is sufficient. The final comparison reduces to
\(2401< (11/200)\,80\cdot2951\).
Here \(p\ge0\), so \(1+pq>0\), \(q+p>0\), and
\(v<13/20\). Equations (18),(22) give
\[
 m_{hh}(\beta,h)
       <\frac1{2\pi}\sqrt{\frac{33}{7}}
       <\frac{11}{10\pi}.
 \tag{23}
\]
The last comparison is \(825<847\). Integrating from height
zero and using (20),
\[
 m(\beta,K)
 \le b_2-\frac{1-\cos\beta}{2\pi}
                   +\frac{539}{2000\pi}.
 \tag{24}
\]

At \(a=a_0\), \(0\le h\le h_0\), the same elementary series
gives \(\cosh(1/10)<101/100\), and hence \(v<151/200\).
Here the two positive-denominator conditions for (10),(17)
also hold. Thus
\[
 m_{hh}(a_0,h)
      <\frac{\sqrt{351}}{14\pi}<\frac{19}{14\pi},
 \qquad
 m(a_0,h_0)
       \le b_2-\frac{67}{72\pi}+\frac{19}{2800\pi}.
 \tag{25}
\]
This uses \(351<361\).

The first shortened edge retains its own complete-end phase.
On the fixed slit compact containing (3), the
[all-row slit theorem](research_mixed_next_first_short_edge_slit_plane_bound.md)
gives, for every fixed \(\tau>0\),
\[
 |K_N^<(a-ih_0,0)|
       \le C_\tau e^{N(\Re\psi(a-ih_0,0)+\tau)}.
 \tag{26}
\]
The explicit original first-edge bound in Section 4 of the
diagonal-taper theorem, before inserting the outgoing edge,
is
\[
 2\Re\psi(a_0-ih_0,0)
 <\frac73-\frac{13877}{18000}+\frac2{625}
 =\frac{140903}{90000}<\frac{47}{30}.
 \tag{27}
\]
This estimate follows from the secant Taylor lower bounds
and the original \(b_2<7/12\) normalization; no value of an
action is numerically inserted.

## 4. Comparing the complete row envelope with the actual action

The source bounds (8),(26) and the exact crossing and trace
penalties have rate
\[
 \mathcal R(a,u)=
  \Re\psi(a-ih_0,0)+m(a,h_0)+m(\beta,K)
                       +\frac{3ah_0}{2\pi}-h_0 .
 \tag{28}
\]
At \(a=a_0\) the last two terms cancel. Since
\[
 \frac{19}{2800}+\frac{539}{2000}
       =\frac{967}{3500}<\frac7{25},
 \tag{29}
\]
equations (24)--(27) give
\[
 \mathcal R(a_0,u)
 <\frac{39}{20}-\frac{1171}{1800\pi}
                         -\frac{1-\cos\beta}{2\pi}.
 \tag{30}
\]

Crucially, compare this with the real-angle loss retained
in the proof of the taller-strip action bound, rather than
its constant final floor. That proof gives
\[
 s(\beta-iK)>
 \frac{46}{25}-D_{\rm real}(\beta)-\frac2{27\pi},
 \qquad
 D_{\rm real}(\beta)
       =-\frac{32}{17\pi}\log\cos(\beta/2).
 \tag{31}
\]
The difference between this real loss and the row loss
in (30) satisfies
\[
 D_{\rm real}(\beta)-\frac{1-\cos\beta}{2\pi}
                                      <\frac{27}{170\pi}.
 \tag{32}
\]
For completeness its derivative is
\[
 \frac{\sin\beta}{\pi}
          \left\{\frac{16}{17(1+\cos\beta)}-\frac12\right\}.
 \tag{33}
\]
The bracket increases and has at most one zero; its sign
changes from negative to positive. Thus the difference
in (32) has its maximum at an endpoint of \([0,\pi/2]\).
At zero it is zero. At \(\pi/2\) use the written witness
\(\log2<7/10\) from the taller-strip theorem to obtain
\[
 \pi D_{\rm real}(\pi/2)-\frac12
       =\frac{16\log2}{17}-\frac12<\frac{27}{170}.
 \tag{34}
\]
It follows from (30)--(32), using \(\pi<22/7\), that
\[
 \begin{split}
 s(u)-\mathcal R(a_0,u)
 &>-\frac{11}{100}
   +\frac1\pi
       \left\{\frac{1171}{1800}-\frac2{27}-\frac{27}{170}\right\}\\
 &>-\frac{11}{100}
                  +\frac7{22}\frac{38341}{91800}
   =\frac{46231}{2019600}>\frac1{50}.
 \end{split}
 \tag{35}
\]
The last cleared comparison is \(46231>40392\).

This gap persists throughout the horizontal segment.
Indeed \(m(a,h_0)\) is nonincreasing by (12). Also,
for \(a_0\le a\le a_1\), put \(q=\cosh h_0<101/100\).
One has \(\cos a\ge-\sqrt3/2>-7/8\), so
\[
 1+q\cos a>93/800>0.
 \tag{36}
\]
The function
\[
 X(a)=\Re\tan((a-ih_0)/2)
               =\frac{\sin a}{q+\cos a}
 \tag{37}
\]
is therefore increasing on this interval. At its left
endpoint it is greater than
\(\sqrt3/(51/50)>1\).
For the principal return \(r=\operatorname{arsinh}(X+iY)\),
\(X>0\) implies
\(\Re r\ge\operatorname{arsinh}X\): write
\(X=\sinh(\Re r)\cos(\Im r)\) with
\(|\Im r|<\pi/2\).
Thus
\[
 \partial_a\Re\psi(a-ih_0,0)
   =-\pi^{-1}\Re\operatorname{arsinh}\tan((a-ih_0)/2)
                                  <-\frac3{4\pi}.
 \tag{38}
\]
Here \(\operatorname{arsinh}1>3/4\) follows from
\(\sinh(3/4)\le24/29<1\).
The additional derivative in (28) is only \(3/(20\pi)\).
Consequently
\[
             \mathcal R(a,u)\le\mathcal R(a_0,u)
                        \qquad(a_0\le a\le a_1).
 \tag{39}
\]
One may also differentiate the maximizing row: (36) and
\((q-\cos a)/2<377/400<1\) ensure that (10) is smooth
on this whole first-angle segment. Monotonicity (12)
already suffices, without this extra observation.

## 5. Complete current and scope

On (3) the exact denominator obeys
\[
 |W_N(a-ih_0)|
       \le\frac{e^{-Nh_0}}{(1-e^{-Nh_0})^2}.
 \tag{40}
\]
The numerator crossing has modulus \(e^{3Nah_0/(2\pi)}\).
Equations (8),(26),(35),(39),(40) therefore bound the
absolute current by a polynomial factor times
\(e^{N(s(u)-1/50+\tau)}\).
Take \(\tau=1/400\); the fixed path length, bounded sine,
row counts, original \(N^2/\pi\) factor and remaining
polynomial losses are absorbed into a further \(1/400\)
allowance for large \(N\). The resulting gap exceeds
\(1/100\), proving (4).

The calculation uses the literal cutoff \(U=\lfloor N/2\rfloor-1\).
There is no hidden normal evaluation or odd simple-node deletion
in the Cauchy--Schwarz step: it bounds exactly the two-short
integrand of the original contour representation. Its relationship
to full inner kernels continues to require the separately proved
full Hermite trace deletions. The diagonal taper ends precisely
at the starting point of (3), and both paths stay in the open
lower half-plane, with their original orientations.

This theorem supplies the previously missing low horizontal at
outgoing heights through \(7/10\). It does not by itself estimate
the remaining far connector, construct the whole inner packet,
or prove the ordinary closing asymptotic.

## Frozen source bindings

- Taller calibrated cubic/action and retained angular loss:
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Real Newton profile, uniform product bound, and exact real maximum:
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e.
- Compact-height zero-safe full-row product bound:
  5e64e4909b55107431d13fcbff92f41776ff101757c5a9f7eb70ae2d8ea1408d.
- Complete first-short slit upper bound:
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Diagonal taper and explicit low first-edge bound:
  7ba93b34b12765ebdfec7853ffc1e7e77bc370e07770c9088f59e538785af908.
- Exact original current normalization:
  2c5be7138aed7dabbb06f04010c602ee095fa8ceb62ec213e75e4d628aa95421.
