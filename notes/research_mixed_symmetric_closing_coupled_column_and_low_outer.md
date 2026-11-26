# A coupled complete-column bound and the low outer horizontal

Private written deduction, 10 November 2026. The two-crossing matrix
and the complete incoming column attain their largest absolute rates
at different colors. Retaining this distinction gives a fixed loss
in the actual three-crossing column. It pays the complete low outer
horizontal starting at real angle \(2\pi/3\).

The vertical connection from the previously studied outer hyperbola
to this low horizontal is not estimated here. No phase estimate is
substituted for a finite-source bound.

## 1. Exact source and statements

Keep the original matrices, Newton vector, and complete kernel:
\[
 Q_N(w,u)=\mathbf e(-2\cos u)^TJ_NM_N^3\mathbf e(w),\qquad D=N-1.
 \tag{1}
\]
Write
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 b_2=-4J(1/4),\qquad
 \lambda_*=\Re S_{\rm cap}(1/2).
 \tag{2}
\]
The cap phase and its logarithmic lift are precisely those of the
[complete-column theorem](research_mixed_symmetric_closing_complete_column_norm.md).
In particular
\[
 b_2<7/12,\qquad \lambda_*<175/216,\qquad
 \lambda_*>b_2+1/9,\qquad b_2>56/99 .
 \tag{3}
\]

**Theorem 1.** For each fixed \(\tau>0\), a fixed ordinary complex
disk \(\mathcal D_\tau\) about \(-2\) and constants \(C,A\) exist
such that, at both level parities,
\[
 \sup_{w\in\mathcal D_\tau}\|M_N^3\mathbf e(w)\|_2
 \le C N^A
       \exp N\{b_2+\lambda_*-1/19+\tau\}.
 \tag{4}
\]
Every fixed ordinary incoming derivative has the same bound on a
smaller disk. All original rows are included.

For the actual closing source put
\[
\begin{aligned}
 F_N(u;\mathbf w)&=Q_N(w_L,u)Q_N(w_R,u),\\
 G_N(u;\mathbf w)&=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2},
                    \qquad \eta_N=(-1)^{N-1}.
\end{aligned}
 \tag{5}
\]
Let \(M_g=\Re\Xi(u_g)\) retain its original geometric normalization.
The adopted action floor is \(M_g>163/50\). Define
\[
 h_0=1/10000,\qquad
 \gamma_0:\quad 2\pi/3-ih_0\longrightarrow4\pi/5-ih_0.
 \tag{6}
\]

**Theorem 2.** On sufficiently small fixed ordinary incoming
neighborhoods of \(w_L=w_R=-2\), for both parities and all
sufficiently large \(N\),
\[
 \frac{N^2}{\pi}\int_{\gamma_0}
             |G_N(u;\mathbf w)W_N(u)|\,|du|
       \le C e^{N(M_g-1/400)}.
 \tag{7}
\]
The same conclusion holds for fixed mixed ordinary incoming
derivatives on smaller neighborhoods. The signed current retains
the original additional scalar \(-C_{N,4}/i\), of modulus one.

## 2. The complete two-crossing profile

The exact original matrix identity is
\[
 (J_NM_N^2)_{ij}
   =Nq^{(i-j)^2}
       \frac{(q^2;q^2)_{i+j}}
            {(q^2;q^2)_i^2(q^2;q^2)_j^2}
                 \quad(i+j<N),
 \tag{8}
\]
and the entry is zero otherwise. Its uniform absolute exponent,
including every boundary of the supported triangle, is
\[
 G(x,y)=J(x+y)-2J(x)-2J(y),\qquad x,y\ge0,\quad x+y\le1.
 \tag{9}
\]
The uniform error in the logarithm of a nonzero entry is
\(O(\log N)\). The complete matrix proof gives \(G\le b_2\).

We need a stronger comparison with the complete column profile
\[
 f(y)=\Re S_{\rm cap}(y)+J(y).
 \tag{10}
\]
Its unique maximum is \(f(1/2)=\lambda_*\).

First, for \(y>1/2\), put \(z=1-y\). If \(0\le x\le z\), then
\[
 G(x,y)-G(x,z)=4J(z)-J(z-x)-J(z+x)\le2J(z)\le0.
 \tag{11}
\]
Indeed \(J(1-z)=-J(z)\), and
\[
 \frac{d}{dx}\{J(z-x)+J(z+x)\}
       =\log\frac{\sin\pi(z+x)}{\sin\pi(z-x)}\ge0
                 \quad(0<x<z\le1/2).
\]
The last inequality follows from
\(\sin\pi(z+x)-\sin\pi(z-x)=2\cos\pi z\sin\pi x\).
Endpoint limits are integrable. Also \(J(z)\le0\) for
\(0\le z\le1/2\). By symmetry the same folding applies to
\(x>1/2\).

For \(0<y\le1/2\), let
\[
 g(y)=\max_{0\le x\le1-y}G(x,y).
 \tag{12}
\]
After the \(x\)-fold, the maximizing \(x\) is the unique interior
point of \((0,1/2)\) satisfying
\[
             \sin\pi(x+y)=2\sin^2\pi x.
 \tag{13}
\]
To see uniqueness, set
\[
 p=\cot\pi x,\quad q=\cot\pi y,\quad
 r=\cot\pi(x+y)=\frac{pq-1}{p+q}.
\]
On \(0<x<1/2\),
\[
 G_{xx}=\pi(r-2p)
       =-\pi\frac{2p^2+pq+1}{p+q}<0.
\]
The first derivative tends to \(+\infty\) at \(x=0\) and is
negative at \(x=1/2\); these facts also cover \(y=1/2\).
The envelope differentiation therefore gives
\[
 g''(y)=-2\pi\,\frac{pq+1}{2p-r}<0,\qquad
                g(1/4)=b_2,\quad g'(1/4)=0.
 \tag{14}
\]
This establishes concavity on the whole interval \((0,1/2)\).

On \(1/4\le y\le3/8\) the maximizing \(x\) obeys
\[
             1\le p\le6/5,\qquad 2/5\le q\le1.
 \tag{15}
\]
The upper bound \(x\le1/4\) follows by testing \(G_x\) there.
For the other bound set \(x_0=\pi^{-1}\operatorname{arccot}(6/5)\).
Then \(2\sin^2\pi x_0=50/61\). By concavity of the sine on
the interval in question, it suffices to check its two ends:
\[
\begin{aligned}
 \sin\pi(x_0+1/4)&=11/\sqrt{122}>11/12>50/61,\\
 \sin\pi(x_0+3/8)
  &=\frac{5\cos(3\pi/8)+6\sin(3\pi/8)}{\sqrt{61}}
    >291/320>50/61.
\end{aligned}
\]
Here \(\cos(3\pi/8)>3/8\), \(\sin(3\pi/8)>9/10\), and
\(\sqrt{61}<8\); the first two inequalities follow respectively
from \(\sqrt2<10/7<23/16\) and \(\sqrt2>7/5\).
Thus \(G_x(x_0,y)>0\), proving \(x>x_0\).
Finally \(\cot(3\pi/8)=\sqrt2-1>2/5\).

For fixed positive \(p\), the ratio in (14) increases with \(q\):
its numerator increases and \(r_q=(p^2+1)/(p+q)^2>0\).
At \(q=2/5\) it is
\[
 L(p)=\frac{10p^2+29p+10}{5(10p^2+2p+5)}.
 \tag{16}
\]
The numerator of its derivative, apart from a positive factor,
is \(-270p^2-100p+125<0\) for \(p\ge1\).
Consequently
\[
 \frac{pq+1}{2p-r}\ge L(6/5)=296/545>27/50,
 \qquad
             g''(y)\le-\frac{27\pi}{25}
                    \quad(1/4\le y\le3/8).
 \tag{17}
\]
The last rational comparison is \(14800>14715\).

## 3. Global curvature of the actual cap column

Use the same branch as the complete-column source:
\[
 \sqrt{1-2e^{2\pi i y}}=a+ib,\qquad
 \sigma=\sqrt{1-b^2}\in(0,1].
\]
Its exact identities give
\[
 f'(y)=\frac12\log\frac{1-b}{1+b},\qquad
               2\sin^2\pi y=\sigma(1+\sigma).
 \tag{18}
\]
The sign of \(b\) is negative before \(1/2\) and positive after
it. Differentiating the second identity and using
\[
 \sin(2\pi y)=-b\sqrt{\sigma(\sigma+2)}
\]
gives
\[
 f''(y)=
   -\,\frac{2\pi\sqrt{(\sigma+2)/\sigma}}{1+2\sigma}
             \le-\frac{2\pi}{\sqrt3}.
 \tag{19}
\]
The displayed inequality is equivalent, after squaring positive
quantities, to
\[
 3(\sigma+2)-\sigma(1+2\sigma)^2
       =2(1-\sigma)(2\sigma^2+4\sigma+3)\ge0.
\]
The limiting value at \(y=1/2\) agrees with the original
complete-column Hessian. The same identities give
\(b(1-y)=-b(y)\), hence \(f(1-y)=f(y)\). In particular
\[
          f(y)\le\lambda_*-\frac{\pi}{\sqrt3}(y-1/2)^2.
 \tag{20}
\]

We now prove the uniform supported-triangle bound
\[
                  G(x,y)+f(y)\le b_2+\lambda_*-1/19.
 \tag{21}
\]
By (11) and symmetry of \(f\), it suffices to take \(y\le1/2\).
For \(y\le1/4\), (20) and \(G\le b_2\) give a loss at least
\(\pi/(16\sqrt3)>1/19\).

Put \(c_g=27\pi/50\), \(c_f=\pi/\sqrt3\).
On \(1/4\le y\le3/8\), (17) gives
\[
 b_2-g(y)\ge c_g(y-1/4)^2.
\]
Together with (20), the loss is at least
\[
 \frac{\pi}{16(50/27+\sqrt3)}
  >\frac{4239}{77800}>\frac1{19}.
 \tag{22}
\]
Here \(\sqrt3<7/4\), \(\pi>157/50\), and the last comparison
is \(80541>77800\).

For \(3/8\le y\le1/2\), concavity and the integrated derivative
in (17) give the tangent bound
\[
 b_2-g(y)\ge
       c_g\left\{\frac{y-1/4}{4}-\frac1{64}\right\}.
 \tag{23}
\]
Adding \(c_f(1/2-y)^2\) and completing the square gives the
uniform lower bound
\[
 \frac{\pi}{64}
       \left\{\frac{81}{50}-\frac{729\sqrt3}{2500}\right\}
  >\frac{1742229}{32000000}>\frac1{19}.
 \tag{24}
\]
The same elementary bounds on \(\pi,\sqrt3\) were used; the
last cross product is \(33102351>32000000\).
This proves (21).

## 4. Finite rows, ordinary colors, and proof of Theorem 1

The exact column identity is
\[
 (M_N\mathbf e(w))_j=\kappa(-q)^jS_j C_{j,N}(w).
 \tag{25}
\]
On each retained compact index interval, the full-index cap
packet, including its ordinary-color neighborhood, gives
\[
 |(M_N\mathbf e(w))_j|
       \le C_\tau N^A e^{N(f(j/N)+\tau)}.
 \tag{26}
\]
The disk is fixed before \(N\); its size may depend on \(\tau\).
This is exactly the compact-row statement used in Section 6
of the complete-column theorem.

Retain that theorem's literal two endpoint groups, with
\(\delta_0=1/100\). At \(j/N\le\delta_0\) the rate is
\(9/50+\tau\). At \((D-j)/N\le\delta_0\) it is
\(b_2+1/20+\tau\). Both are strictly less than
\(\lambda_*-1/19+\tau\): for the second,
\[
 \lambda_*-(b_2+1/20)>11/180>1/19;
\]
for the first, \(\lambda_*>67/99>2/3\) is more than sufficient.
These bounds retain every upper row, including odd revived
factors, by the exact reflection formula in that source.
Their small ordinary-color neighborhoods and fixed derivatives
are established there by literal products and regularized
Newton sums, not by continuing a single complete value.

Apply (8), (21), and (26) to
\[
       J_NM_N^3\mathbf e(w)=(J_NM_N^2)(M_N\mathbf e(w)).
 \tag{27}
\]
On the two endpoint groups use \(G\le b_2\) and their just
stated stronger losses. Every component of (27) is bounded
by a polynomial times the right side of (4). Summing the at
most \(N\) terms and then taking the vector norm changes
only that polynomial. Reversal \(J_N\) preserves the norm.
This proves (4), and Cauchy's formula on smaller fixed disks
proves its derivative assertion.

## 5. The complete low outer current

The full Newton-vector estimate gives
\[
 \|\mathbf e(-2\cos(a-ih))\|_2
       \le C N^B e^{N(m_0(a)+h)}.
 \tag{28}
\]
It includes all indices. The exact real maximum is decreasing
in \(a\), and the real-profile integration gives
\[
 m_0(a)\le m_0(2\pi/3)
        \le b_2-\frac{67}{72\pi}
                         \qquad(2\pi/3\le a\le\pi).
 \tag{29}
\]
Apply Cauchy--Schwarz to (1) with Theorem 1. For the two inner
factors the rate is at most
\[
 2\{2b_2+\lambda_*-1/19-67/(72\pi)+\tau\}+2h.
\]
The original outer crossing and full sampling factor together
have rate \((2a/\pi-1)h\). Indeed, at the fixed positive height
\(h_0\),
\[
 |W_N(a-ih_0)|
       \le e^{-Nh_0}(1-e^{-Nh_0})^{-2}\le C e^{-Nh_0}.
 \tag{30}
\]
Thus the complete rate on (6), before \(\tau\) and polynomial
allowances, is bounded above by
\[
 2\left\{\frac{427}{216}-\frac{469}{1584}-\frac1{19}\right\}
       +3h_0
   =2\left\{\frac{7987}{4752}-\frac1{19}\right\}+3h_0.
 \tag{31}
\]
We used \(b_2<7/12\), \(\lambda_*<175/216\), and \(\pi<22/7\).
Its zero-height margin below \(163/50\) is
\[
 \frac{163}{50}
    -2\left\{\frac{7987}{4752}-\frac1{19}\right\}
       =\frac{4211}{1128600}>\frac1{300},
 \tag{32}
\]
where \(1263300>1128600\).
Choose \(\tau=1/10000\) for each of the two column factors.
The height costs \(3/10000\). Absorb the polynomial factors,
path length, sine, and the original \(N^2/\pi\) using a further
\(1/10000\). The retained margin exceeds
\[
             \frac1{300}-\frac6{10000}
                 =\frac{41}{15000}>\frac1{400}.
 \tag{33}
\]
This proves (7) uniformly on the chosen incoming bidisk.
The pointwise source estimate, followed by Cauchy on smaller
disks, proves the mixed derivative statement.

The vertical at \(a=4\pi/5\) from height \(h_0\) to \(1/100\)
is also paid by the proof of the
[earlier far-right theorem](research_mixed_symmetric_closing_earlier_far_right_connection.md):
its upper-rate calculation is unchanged, and its sampling
denominator now uses the fixed positive lower height \(h_0\).
Following it by that theorem's original far path reaches the
original midpoint endpoint \(a_N-ih_c\), with all full-source
scalars retained. This extends the controlled near-real right
path to \(2\pi/3-ih_0\).

What remains separate is a paid path from the outer hyperbola
endpoint \(2\pi/3-3iK_g/4\) down to this new starting point.
The present norm estimate, by itself, is not asserted on that
deeper vertical.

## Source bindings

- Exact supported two-crossing matrix and its full factorial estimate:
  [global preparation bound](research_three_crossing_global_preparation_error.md),
  c1e80c6efbc9ff936d889eebd1f449e85c81820a64fb046e6dfe8e1003d2d239.
- Literal complete column, cap profile, endpoint groups, ordinary
  incoming neighborhoods and constants:
  [complete-column norm](research_mixed_symmetric_closing_complete_column_norm.md),
  4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519.
- Original full-index cap packet used in (26):
  [full-index theorem](research_complete_boundary_full_index_interval.md),
  450cd41db9c49049e9b80a41c83828a2f0fafa43f986803bc57b93be580a57ef.
- Complete evaluation vector and exact real maximum:
  [real-period theorem](research_three_crossing_real_period_newton_bound.md),
  8759b9d7784d0c96590410969b172c95a697d86261936fd1e09201d9d12dcc2e;
  [left-far vector estimate](research_mixed_symmetric_closing_left_far_connection.md),
  d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184.
- The explicit real profile value used in (29):
  [low inner norm proof](research_mixed_symmetric_closing_low_horizontal_norm.md),
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- The original geometric floor and the written rational lower
  bound for \(\pi\):
  [closing action floor](research_mixed_symmetric_closing_action_floor_163.md),
  f0bfaf90d7e331adf1df3ba59980dea76ebc8347b7244d2b52c4e1c692b5f825.
- Original full outer source and controlled continuation:
  [earlier far-right connection](research_mixed_symmetric_closing_earlier_far_right_connection.md),
  9b62082201e99c73371c19cd82f7279fb3a4a57cecff2135306815f3bc3ad416.
