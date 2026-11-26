# The coherent high-index rate has no unpaid interior maximum

Research deduction, 7 November 2026. The actual exterior root of the
Wall degree recurrence satisfies an analytic logarithmic derivative
bound on the first quarter of its degree interval. Combined with the
original incoming polynomial, this reduces the entire high retained
index interval to its two endpoint rates. The true endpoint has already
been paid. Only the coherent rate at retained index \(s=1/2\) remains
to be compared with the original supporting plane.

No root, analytic function, rate, or candidate is evaluated here.
The finite outgoing sum remains contracted before taking a modulus.

## 1. The original branch and elementary parameter bounds

Keep \(Y=\rho e^{i\phi}=p+iv=e^{2\pi ix_0}\), with its original
logarithmic lift. The inherited bounds from
[allocation curvature](research_mixed_fourier_allocation_curvature.md)
and the [high-index branch theorem](research_mixed_fourier_right_cap_wall_high_index_branch.md)
are
\[
 \frac{121}{200}<\rho<\frac{123}{200},\qquad
 \frac25<\cos\phi<\frac{21}{50},\qquad
 \frac9{10}<\sin\phi<\frac{921}{1000}.
 \tag{1}
\]
Write
\[
 c=Y^{-1}-1=a_0-ib_0,\qquad
 -\frac7{20}<a_0<-\frac{37}{121},\qquad
 \frac{60}{41}<b_0<\frac{921}{605}<\frac{61}{40}.
 \tag{2}
\]
The notation \(a_0,b_0\) in (2) does not denote the incoming leg.
For \(0\le t\le1/4\), put
\[
 S=e^{2\pi it},\qquad z=S^{-1}.
 \tag{3}
\]
The established original outgoing branch is the unit-disk root of
\[
 Q^2-(2+c-S)Q+c=0,\qquad Q(0)=1.
 \tag{4}
\]
For \(t>0\), the high-index branch theorem proves
\[
 |Q|<1,\qquad q=-\frac{\log Q}{2\pi i},\qquad
 0<\Re q<t,\qquad \Im q<0.
 \tag{5}
\]
The completed [half-degree theorem](research_mixed_fourier_right_cap_wall_half_degree_completion.md)
identifies the actual exterior degree root with
\[
 R(t)=\frac{z-1}{z-Q}
      =\frac{1-S}{1-SQ},\qquad |R(t)|>1,
 \tag{6}
\]
with its nonzero continuation at \(t=0\). This is the root selected
by the exact finite initial condition, not a new root choice.

Define
\[
 H=\frac{c-Q^2}{Q},\qquad L=\frac HS.
 \tag{7}
\]
Then
\[
 H^2=(S-2-c)^2-4c,\qquad H(0)=c-1,\qquad
 q_t=-\frac SH=-\frac1L.
 \tag{8}
\]
Indeed differentiating (4), or its inverse
\(S=2+c-Q-c/Q\), gives \(Q_t=2\pi iSQ/H\).
All these derivatives use the original continuous branch.

## 2. A derivative disk for the outgoing saddle

**Lemma 1.** Throughout \(0\le t\le1/4\),
\[
                      \Re L<-\frac12,\qquad |1-q_t|<1.
 \tag{9}
\]

*Proof.* Set \(\theta=2\pi t\), \(x=\cos\theta\), \(y=\sin\theta\),
and
\[
 U=4+a_0^2-b_0^2,\qquad V=-2a_0b_0.
 \tag{10}
\]
The exact bounds (2) imply
\[
 \begin{gathered}
 0<U<2,\qquad 0<V<\frac{11}{10},\\
 \frac{33}{10}<2(2+a_0)<\frac{17}{5},\qquad
                              2b_0>\frac{29}{10}.
 \end{gathered}
 \tag{11}
\]
For the only close comparison in \(U<2\), use
\[
 2+\frac{49}{400}<\frac{3600}{1681},
 \qquad 849\cdot1681=1427169<1440000.
\]
The other upper bounds follow from
\(V<427/400<11/10\) and \(410/121<17/5\).
In particular every inequality in (11) is an elementary consequence
of the existing parameter enclosure.

Write \(Z=L^2\). From (8),
\[
 Z=1-2(2+c)S^{-1}+(4+c^2)S^{-2},
 \tag{12}
\]
and hence
\[
 \begin{split}
 \Re Z&=1-2(2+a_0)x+2b_0y+U(x^2-y^2)+2Vxy,\\
 \Im Z&=2(2+a_0)y+2b_0x+V(x^2-y^2)-2Uxy.
 \end{split}
 \tag{13}
\]
Both \(x,y\) are nonnegative.

If \(x\ge y\), (11)--(13) give \(\Re Z>-12/5\) and
\[
 \Im Z>\frac{29}{10}(x+y)-4xy.
 \tag{14}
\]
For \(u=x+y\in[1,\sqrt2]\), the right side is
\(2+29u/10-2u^2\), a concave quadratic. Its values at the two
endpoints are \(29/10\) and \(-2+29\sqrt2/10\); both exceed 2,
using \(\sqrt2>7/5\). Thus in this case
\[
                 \Im Z>2,\qquad
                 \Re Z+(\Im Z)^2>\frac85>\frac14.
 \tag{15}
\]

If \(x\le y\), then \(x\le1/\sqrt2<5/7\) and
\[
 y=\sqrt{1-x^2}\ge1-\frac35x^2.
 \tag{16}
\]
To verify (16), square its nonnegative right side and use
\(x^2\le1/2<5/9\). Also \(xy\le x\). Consequently
\[
 \begin{split}
 \Im Z
 &>\frac{33}{10}y+\frac{29}{10}x
                  -4xy-\frac{11}{10}(y^2-x^2)\\
 &\ge\frac{11}{5}-\frac{11}{10}x+\frac{11}{50}x^2
 \ge\frac{374}{245}>\frac32.
 \end{split}
 \tag{17}
\]
The last quadratic decreases on \([0,5/7]\), and its value at
\(5/7\) is \(374/245\). The real part satisfies
\[
 \Re Z>1-\frac{17}{5}x+\frac{29}{10}y-2
       \ge-1-\frac x2>-\frac{19}{14}.
 \tag{18}
\]
Thus in this case
\[
               \Re Z+(\Im Z)^2>
                         -\frac{19}{14}+\frac94=\frac{25}{28}>\frac14.
 \tag{19}
\]

Equations (15), (17), and (19) prove on the whole interval that
\(\Im Z>0\) and \(\Re Z+(\Im Z)^2>1/4\).
At zero, \(L=c-1\) has negative real and imaginary parts. Its square
remains in the upper half-plane, so the same quadrant of \(L\)
continues throughout. If \(L=u+iw\) had \(-1/2\le u<0\), then
\[
 \Re Z+(\Im Z)^2
       =u^2+(4u^2-1)w^2\le u^2\le\frac14,
 \]
contrary to the strict bound. Therefore \(\Re L<-1/2\).
Finally
\[
 |1-q_t|^2=|1+L^{-1}|^2
          =1+\frac{2\Re L+1}{|L|^2}<1.
 \]
This proves (9). \(\square\)

## 3. The logarithmic derivative of the actual degree root

The elementary disk estimate needed here preserves a useful
cancellation in \(Q R\).

**Lemma 2.** On the branch above, \(|Q R|<2\).

*Proof.* The inverse relation in (4) and (6) give
\[
 QR=\frac{c-Q}{1+c-Q}
      =1-\frac{Y}{1-YQ}.
 \tag{20}
\]
For every \(|Q|\le1\), the last Möbius map has disk center
\((1-k-Y)/(1-k)\) and radius \(k/(1-k)\), where \(k=|Y|^2\).
Therefore its maximum modulus is at most
\[
             \frac{|1-k-Y|+k}{1-k}.
 \tag{21}
\]
The inherited bounds give
\[
 \frac9{25}<k<\frac{19}{50},\qquad p=\Re Y>\frac6{25}.
 \]
In particular \(2-3k>0\), and
\[
 \begin{split}
 (2-3k)^2-|1-k-Y|^2
 &=3-11k+8k^2+2p(1-k)\\
 &>3-\frac{209}{50}+\frac{648}{625}+\frac{372}{1250}
   =\frac{193}{1250}>0.
 \end{split}
 \tag{22}
\]
Thus \(|1-k-Y|<2-3k\), which makes (21) strictly less than 2.
\(\square\)

**Proposition 1.** For \(0<t\le1/4\),
\[
 \frac{d}{dt}\log|R(t)|
       >\pi\cot(\pi t)-\frac{2\pi}{\sin(\pi t)}
       >-2\pi\cot(\pi t).
 \tag{23}
\]

*Proof.* Since \((SQ)_t=2\pi iSQ(1-q_t)\),
\[
 \begin{split}
 \frac{d}{dt}\log|1-SQ|
 &=\Re\frac{-2\pi iSQ(1-q_t)}{1-SQ}\\
 &\le\frac{2\pi|Q R|\,|1-q_t|}{|1-S|}
   <\frac{2\pi}{\sin(\pi t)}.
 \end{split}
 \tag{24}
\]
Here both lemmas and \(|1-S|=2\sin(\pi t)\) were used.
Differentiate (6), observing that
\(\partial_t\log|1-S|=\pi\cot(\pi t)\).
This proves the first inequality in (23). For the second, use
\(3\cos(\pi t)\ge3/\sqrt2>2\). \(\square\)

## 4. Only the coherent half-index face remains

Use exactly the rate and input domain of
[the retained-rate theorem](research_mixed_fourier_right_cap_coherent_retained_rate.md):
\[
 a=x+ih,\quad \frac{11}{50}\le x\le\frac9{20},
 \quad -.108\le h\le.068,\qquad \eta\in\{0,1\}.
 \tag{25}
\]
In particular \(X=e^{-2\pi ia}\), \(|X^{-1}|<2\), and
\[
 \begin{split}
 I_a(s)&=\int_0^s\log|1-Xe^{-2\pi iu}|\,du,\\
 \mathcal E_\eta(s;a)&=
 I_a(s)-3J(s)-2\pi hs+\Re\Phi(s;y)-\frac\eta2\Re g(a).
 \end{split}
 \tag{26}
\]
The integral is continuous across an incoming polynomial zero;
it is not an off-branch dilogarithm substitution.
Set \(G(t)=\mathcal E_\eta(1-t;a)\). The exact calibrated derivative is
\[
 G'(t)=2\log(2\sin\pi t)+\log|R(t)|-\log D_a(t),
 \qquad
 D_a(t)=|1-X^{-1}e^{-2\pi it}|.
 \tag{27}
\]

For \(0<t<\min(x,1/4)\), \(D_a'(t)\le0\):
the angle \(2\pi(x-t)\) lies in \([0,.9\pi]\), and differentiating
the squared modulus gives a nonpositive derivative. Equation (23)
therefore proves
\[
 G''(t)>
       \pi\,\frac{3\cos(\pi t)-2}{\sin(\pi t)}
       >\frac{\pi}{10}>0.
 \tag{28}
\]
For the final bound use \(3/\sqrt2>21/10\).
Thus \(G\) is strictly convex on this part of the interval.

If \(x<t\le1/4\), then \(x\in[11/50,1/4]\) and
\(|2\pi(x-t)|\le3\pi/50<1/5\). Convexity of the squared distance
as a function of \(|X^{-1}|\in[0,2]\) gives
\[
 D_a(t)^2\le\max\{1,5-4\cos(2\pi(x-t))\}
              <\frac{27}{25}<\frac{36}{25}.
 \tag{29}
\]
Indeed \(\cos u\ge1-u^2/2>49/50\) when \(|u|<1/5\).
On the other hand \(t>1/5\), so
\[
 4\sin^2(\pi t)>4\sin^2(\pi/5)
             =\frac{5-\sqrt5}{2}>\frac43.
 \]
Using \(|R|>1\), (27) now gives
\[
                              G'(t)>\log(10/9)>0.
 \tag{30}
\]
If \(D_a=0\), the derivative has an integrable positive logarithmic
divergence. Continuity and absolute continuity of (26) retain the
same monotonicity through that point.

Convexity on \([0,\min(x,1/4)]\), followed when needed by (30),
shows that the maximum of \(G\) on \([0,1/4]\) is at an endpoint.
The existing retained-rate theorem proves that
\(\mathcal E_\eta\) decreases on \([1/2,3/4]\).
Combining the two statements yields the unconditional rate reduction
\[
 \boxed{\qquad
 \mathcal E_\eta(s;a)
   \le\max\{\mathcal E_\eta(1/2;a),\mathcal E_\eta(1;a)\},
                         \qquad \frac12\le s\le1.
 \qquad}
 \tag{31}
\]
Thus no interior algebraic candidate from that theorem needs to be
estimated for this upper bound.

The endpoint is precisely the already paid one:
\[
 \mathcal E_\eta(1;a)
   =2\pi(-h)_++\pi\Im y-\frac\eta2\Re g(a).
 \tag{32}
\]
For completeness, \(I_a(1)=\log^+|X|=2\pi h_+\), by the elementary
circle mean of \(\log|1-Xz|\); it follows by the convergent logarithmic
series for \(|X|<1\), reciprocal factoring for \(|X|>1\), and
continuity at \(|X|=1\). Also \(J(1)=0\) and
\(\Phi(1;y)=-\pi iy\). These facts give (32) with the original scalar.

For actual admissible incoming references and their retained targets,
the [endpoint-payment theorem](research_mixed_fourier_right_cap_endpoint_payment.md)
proves
\[
                \mathcal E_\eta(1;a)
                   <B_\eta(x)-\frac{387}{70000},
 \tag{33}
\]
where \(B_\eta\) is exactly its original supporting plane, including
the incoming halfweight, marginal, and quadratic loss.
Use the zero-safe finite envelope of the retained-rate theorem away
from \(s=1\), and its overlap with the already paid exact endpoint
strip. For each \(\tau>0\) the original high-index portion consequently
satisfies
\[
 \begin{split}
 &|d_N(X)|^{\eta/2}
 \left|\sum_{j=\lceil N/2\rceil}^{N-1}
       X^{-j}\frac{(rX;r)_j}{P_j^3}H_{j,N}(y)\right|\\
 &\qquad\le C_\tau N^{A_\tau}
  \exp N\left[
    \max\left\{\mathcal E_\eta(1/2;a),
                    B_\eta(x)-\frac{387}{70000}\right\}+\tau\right].
 \end{split}
 \tag{34}
\]
Both original parities, the degree shift \(N-j-1\), all outgoing
physical rows, and zeros of the incoming polynomial are retained.
There is no division by the finite halfweight.

The remaining comparison in this high-index source is now the single
coherent face \(\mathcal E_\eta(1/2;a)\) against \(B_\eta(x)\).
Equation (34) does not assert its sign or pay the other original
retained-index currents. It makes no whole-cap or knot noncancellation
claim.
