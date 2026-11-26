# The complete low-node family of coherent coefficient packets

Research deduction, 7 November 2026. The full physical family
\(B=r^b\), with \(0\le b\le\delta N\) for a sufficiently small
fixed \(\delta>0\), has a uniform nonzero coefficient packet.
Its leading multiplier is \(B/(B-u)\). The proof uses a new
sampled boundary value immediately before the exact recurrence
reset and treats the forcing after that reset separately.

The complete coefficient vectors are asymptotically parallel in
their original coordinates. A single, specified phase correction
therefore gives a nonzero prescribed zero Fourier coefficient
throughout the low-node family. This is a coefficient-index
Fourier observation, not the outgoing Newton evaluation or the
remaining signed sum over incoming nodes.

All finite sources, both parities, and actual boundary data are
retained. No numerical evaluation is used.

## 1. The original family and its reset

Put
\[
 \begin{gathered}
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},
 \quad \kappa=q^{D^2/2},\\
 P_j=\prod_{\nu=1}^j(1-r^\nu),\quad S_j=|P_j|,\quad
 p_j(Y)=\prod_{\nu=1}^j(1-r^\nu Y),\qquad P_0=S_0=1 .
 \end{gathered}
 \tag{1}
\]
The original polynomial \(d_N\), of degree at most \(D\), has
\(d_N(r^b)=P_b^{-1}\). For a physical index \(0\le b<N\), set
\[
 \begin{split}
 B&=r^b,\qquad \theta=b/N,\\
 K_B(Y)&=\frac{B\{d_N(Y)-d_N(B)\}}{Y-B},\\
 A_j(B)&=\operatorname{CT}_Y[K_B(Y)Y^{-j}p_j(Y)],
 \qquad a_j(B)=A_j(B)/P_j,\quad 0\le j<N .
 \end{split}
 \tag{2}
\]
The divided difference is the entire polynomial of degree at most
\(N-2\), including its value \(B d_N'(B)\) at \(Y=B\).
These are precisely the coefficients in
[the original cardinal-sector source](research_mixed_next_low_cardinal_coherent_response.md),
equations (3)--(4), with
\[
 \mathcal S_{1,\beta}[\mathfrak l_b](Z)
    =\sum_{j=0}^{D}a_j(B)\frac{p_j(Z)}{P_j^{1+\beta}},
 \qquad \beta=0,1 .
 \tag{3}
\]
The letter \(\beta\) in (3) is the next-vertex flag; \(\theta\)
always denotes the incoming physical fraction \(b/N\).

Keep the actual coherent column
\[
             \gamma=MJM^3e_0,\qquad v_j=(-q)^{-j}\gamma_j .
 \tag{4}
\]
Equations (6) and (11) of that source give, without an additional
normalizing factor,
\[
 \begin{split}
 a_0(B)&=P_b^{-1}-\frac{\gamma_0}{\kappa^2N^2},\\
 a_j(B)&=h_B(t_j)a_{j-1}(B)
           -\frac{v_j+c(t_j)v_{j-1}}{\kappa^2N^2},\\
 t_j&=j/N,\quad X(t)=e^{-2\pi it},\quad
 c(t)=\frac{X(t)}{1-X(t)},\quad
 h_B(t)=\frac{B^{-1}-X(t)}{1-X(t)} .
 \end{split}
 \tag{5}
\]
For real \(t\) at the physical rows,
\[
                h_B(t)=e^{\pi i\theta}
                            \frac{\sin\pi(t+\theta)}{\sin\pi t}.
 \tag{6}
\]
If \(b\ge1\), its exact zero is at \(j=N-b\). In particular
the actual value immediately after this reset is
\[
 a_{N-b}(B)
       =-\frac{v_{N-b}+c((N-b)/N)v_{N-b-1}}{\kappa^2N^2}.
 \tag{7}
\]
One cannot propagate a terminal value backwards through this zero.
The proof below never divides by (7)'s vanishing multiplier.

There is still an exact terminal identity:
\[
 a_D(B)=
 \begin{cases}
 \displaystyle \frac{B(1-P_b^{-1})}{N(1-B)},&b\ge1,\\[6pt]
 d_N'(1)/N,&b=0 .
 \end{cases}
 \tag{8}
\]
Indeed \(P_D=N\), \(p_D(Y)=\sum_{k=0}^{D}Y^k\), so that
\(A_D(B)=K_B(1)\). The derivative case is the
[terminal-anchor theorem](research_mixed_next_low_cardinal_terminal_anchor.md).
Equation (8) is retained as the actual last datum; for \(b>0\)
the more useful reverse anchor lies before the reset.

## 2. A sampled anchor before the reset

In this section suppose \(0\le b\le N/2\), and put \(m=D-b\).
The Laurent band of \(K_B(Y)Y^{-m}p_m(Y)\) is contained in
\([-m,D-1]\). Its only frequency divisible by \(N\) is zero.
Physical zeros of \(p_m\) consequently give the exact identity
\[
             N A_m(B)
                 =\sum_{a=0}^{b}K_B(r^a)r^{-am}p_m(r^a).
 \tag{9}
\]
Every term \(a>b\) in the full root sum is zero, rather than
being omitted by an estimate.

For \(0\le a\le b\), sine reflection gives
\[
 \frac{|p_m(r^a)|}{S_m}
     =\frac{S_{m+a}}{S_aS_m}
     =\frac{S_b}{S_aS_{b-a}}
     =:\binom ba_{\!S},\qquad
                   1\le\binom ba_{\!S}\le\binom ba .
 \tag{10}
\]
The upper inequality follows term by term from the decrease of
\(\sin x/x\) on \((0,\pi)\):
\[
 \frac{\sin(\pi(b-a+\nu)/N)}{\sin(\pi\nu/N)}
                \le\frac{b-a+\nu}{\nu},\qquad1\le\nu\le a .
 \tag{11}
\]
For the lower inequality, both arguments are in \((0,\pi/2]\)
and the numerator argument is at least the denominator argument.
The empty products have value one.

Write
\[
 J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad
 c_{\mathrm b}=-2J(1/6),\qquad d_*=\frac{c_{\mathrm b}}2<\frac16 .
 \tag{12}
\]
The whole-disk bound in the terminal-anchor theorem is
\[
                   \|d_N\|_{\{|Y|\le1\}}
                                \le C N^C e^{Nd_*}.
 \tag{13}
\]
Polynomial Bernstein on the unit circle, followed by the maximum
principle for \(d_N'\), bounds its modulus throughout the disk
by \(D\|d_N\|_{\{|Y|\le1\}}\). The line segment from \(B\) to
any \(Y\) in the disk lies in that disk. The integral divided
difference formula therefore gives
\[
                    |K_B(Y)|\le D\|d_N\|_{\{|Y|\le1\}},
                                   \qquad |Y|\le1 .
 \tag{14}
\]
This includes the diagonal value \(B d_N'(B)\).
Combining (9)--(14) proves the uniform actual anchor
\[
                  |a_{D-b}(r^b)|
                       \le\frac DN\,2^b\|d_N\|_{\{|Y|\le1\}}
                       \le C N^C e^{N(d_*+\theta\log2)} .
 \tag{15}
\]
For \(b=0\), (9) is exactly the derivative anchor (8). The
identities also include \(N=2\) and the cases with \(m=0\);
no denominator with index \(N\) has been introduced.

## 3. Exact propagation before and after the reset

Before the reset, the homogeneous product of (5) is
\[
 H_{b,j}=\prod_{\nu=1}^j h_B(\nu/N)
          =B^{-j}\frac{P_{b+j}}{P_bP_j},
                         \qquad0\le j\le m=D-b .
 \tag{16}
\]
It is nonzero on this entire range. Sine reflection gives
\(|H_{b,0}|=|H_{b,m}|=1\). More strongly,
\[
                         |H_{b,j}|\ge1\quad(0\le j\le m).
 \tag{17}
\]
For \(b>0\), the real extension
\[
 \log |H_{b,x}|
      =\sum_{\nu=1}^{b}\log(2\sin(\pi(x+\nu)/N))-\log S_b,
                                  \qquad0\le x\le m ,
 \tag{18}
\]
is concave, since each summand has negative second derivative.
Its endpoint values are zero by reflection, proving (17).
For \(b=0\), the product is identically one.

The uniform sine-factorial estimate, including both true ends,
also gives
\[
 \log|H_{b,j}|
     =N Q_\theta(t_j)+O(\log N),\qquad
 Q_\theta(t)=J(t+\theta)-J(t)-J(\theta).
 \tag{19}
\]
Here \(0\le t_j\le1-\theta-1/N\).
Continuity of \(J\) on \([0,1]\) implies that there is a
nonnegative function \(\omega(\delta)\to0\) as \(\delta\downarrow0\)
such that
\[
                  1\le |H_{b,j}|
                     \le C N^C e^{N\omega(\delta)}
                  \quad(0\le b\le\delta N,\ 0\le j\le m).
 \tag{20}
\]
For example, use the sum of the modulus of continuity of \(J\)
at distance \(\delta\) and
\(\sup_{0\le\theta\le\delta}|J(\theta)|\) in (19).
This is an estimate for the original finite product, including
small \(b\), and does not require a factorial packet at \(b/N>0\).

The remaining indices have an equally explicit bound.
For \(b\ge1\) write \(j=N-b+\ell\), \(0\le\ell\le b-1\).
For \(1\le\ell\le b-1\),
\[
 |h_B((N-b+\ell)/N)|
       =\frac{\sin(\pi\ell/N)}{\sin(\pi(b-\ell)/N)} .
 \tag{21}
\]
Consequently, for \(0\le s\le t\le b-1\),
\[
 \prod_{\ell=s+1}^{t}|h_B((N-b+\ell)/N)|
       =\frac{\binom{b-1}{s}_{\!S}}
                    {\binom{b-1}{t}_{\!S}}\le2^b .
 \tag{22}
\]
Both sine binomials lie between one and the corresponding
ordinary binomial, by (10)--(11).
Start exactly at the forced reset value (7), and propagate
forward using (22). The elementary bound
\(|1-r^j|^{-1}\le N/4\), \(1\le j<N\), then shows
\[
 \max_{j\ge N-b}|a_j(B)|
             \le C N^C 2^b
                    \max_{k\ge N-b-1}|v_k|.
 \tag{23}
\]
For \(b=1\) this is the single reset row and its two forcing
values. For \(b=0\) the range in (23) is empty.

Let
\[
 \begin{gathered}
 \lambda(t)=\frac{3-2X(t)+\sqrt{4/X(t)-3}}2,\qquad
 \mu(t)=\frac{3-2X(t)-\sqrt{4/X(t)-3}}2,\\
 I(t)=\int_0^t\log\lambda(s)\,ds,\qquad
 G(t)=\sqrt{\frac{\lambda(t)}{\lambda(t)-\mu(t)}},\\
 A(t)=\Re I(t)-2J(t),\qquad
 B_{\rm col}(t)=\Re I(t)-J(t).
 \end{gathered}
 \tag{24}
\]
All branches are the original ones, continued from square root
one, logarithm zero and \(G(0)=1\).
The [original column theorem](research_three_crossing_next_crossing_fourier.md)
proves that \(B_{\rm col}\) increases continuously from zero.
Its right-end estimate, with the exact distance \(D-k\), gives
\[
 \max_{k\ge N-b-1}|v_k|
              \le C N^C e^{N B_{\rm col}(\delta)}
                       \qquad(1\le b\le\delta N).
 \tag{25}
\]
Indeed \(D-(N-b-1)=b\), so every index in (25) has right
distance at most \(b\). Equations (23)--(25) pay the full
post-reset tail at a rate at most
\[
                         B_{\rm col}(\delta)+\delta\log2
                                  \longrightarrow0.
 \tag{26}
\]
The terminal value (8) is not chosen to enforce this conclusion;
it belongs to the same finite sequence (2).

## 4. Uniform coarse tails and the order of the parameters

The original \(A\) has a unique nondegenerate maximum
\(x_*\in(1/3,1/2)\). Write
\[
                A_*=A(x_*),\qquad \alpha=-A''(x_*)>0 .
 \tag{27}
\]
The terminal-anchor theorem proves analytically that
\[
                 A_*>\frac{20}{63},\qquad
                 A(1/2)>\frac{\log3}{6}>\frac16>d_* .
 \tag{28}
\]
It also traces the following one-sided estimate through the
original equality-of-moduli region, using the exact transfer
matrices rather than selecting a branch there:
\[
     \max_{j/N\ge r_0}|v_j|\le C_{r_0}N^{C_{r_0}}e^{NA(r_0)}
                       \quad(x_*<r_0<1/2).
 \tag{29}
\]
On the left, the original initialized column packet gives
the analogous bound with rate \(A(l_0)\) for \(j/N\le l_0<x_*\).

Fix once and for all
\[
          0<l_0<l<x_*<r<r_0<1/2 .
 \tag{30}
\]
Only after these fixed intervals have been chosen do we choose
a sufficiently small \(\delta>0\). In particular, we may require
\[
 \begin{gathered}
 d_*+\delta\log2<A(r_0),\qquad
 \sup_{\theta\le\delta}[-J(\theta)]<A(l_0),\\
 \omega(\delta)<\tfrac14
       \min\{A(l)-A(l_0),\,A(r)-A(r_0),\,
                         A_*-A(l),\,A_*-A(r)\},\\
 B_{\rm col}(\delta)+\delta\log2<A_*/2 .
 \end{gathered}
 \tag{31}
\]
All inequalities are available by (28), strict monotonicity of
\(A\), and continuity at zero. Further decreases of this same
\(\delta\) below are harmless. No explicit value or evaluation
of \(\delta\) is needed.

Divide (5) by the nonzero product \(H_{b,j}\) on \(j\le m\):
\[
 \frac{a_j(B)}{H_{b,j}}-\frac{a_{j-1}(B)}{H_{b,j-1}}
       =-\frac{v_j+c(t_j)v_{j-1}}{\kappa^2N^2 H_{b,j}}.
 \tag{32}
\]
By (17), all denominators in the right side have modulus at
least one. Summing from the actual value \(a_0(B)\), or
backwards from the actual sampled value \(a_m(B)\), gives
\[
 \begin{split}
 \max_{j/N\le l}|a_j(B)|
      &\le C N^C e^{N\{A(l)+\omega(\delta)\}},\\
 \max_{\substack{j/N\ge r\\j\le m}}|a_j(B)|
      &\le C N^C e^{N\{A(r)+\omega(\delta)\}},
 \end{split}
 \tag{33}
\]
uniformly in \(0\le b\le\delta N\).
Every forward forcing index remains to the left, and every
backward forcing index remains to the right, of its respective
cut. Equations (15), (20), (29) and the polynomial bound on
\(c(t_j)\) justify these estimates including their endpoints.
Together with (26) and (31), they give a uniform \(\eta>0\)
such that
\[
 \max_{j/N\notin[l,r]}|a_j(r^b)|
                   \le C N^C e^{N(A_*-\eta)}
                    \quad(0\le b\le\delta N).
 \tag{34}
\]
Thus the actual initialization, the pre-reset terminal datum,
and the post-reset forcing are all exponentially paid outside
one fixed interior interval.

The quantifiers matter: the interval in (30) is fixed first.
This theorem does not assert that one \(\delta\) gives the
same relative row asymptotic on every compact interval
arbitrarily close to either endpoint.

## 5. The nonresonant symbol and its exact corrected telescoper

Put
\[
 \begin{gathered}
 d(t)=4\sin^2\pi t,\qquad \rho(t)=d(t)/\lambda(t),\qquad
 u(t)=\frac{1-\sqrt{4/X(t)-3}}2,\\
 \rho_1(t)=\frac{\rho(t)\{\lambda'(t)-\mu'(t)\}}
                         {2\{\lambda(t)-\mu(t)\}} .
 \end{gathered}
 \tag{35}
\]
The original branch has
\[
 X=\frac1{1-u+u^2},\qquad
 \rho=-\frac{u^2}{1-u}.
 \tag{36}
\]
A direct substitution, retaining \(B\), gives
\[
 \boxed{\quad
 F_B(t):=\frac{1+c(t)\rho(t)}{1-h_B(t)\rho(t)}
                         =\frac{B}{B-u(t)} .
 \quad}
 \tag{37}
\]
For clarity, with \(D_u=1-u+u^2\), the numerator and denominator
on the left are respectively
\[
 \frac{D_u}{(1-u)^2},\qquad
                \frac{D_u(B-u)}{B(1-u)^2}.
 \tag{38}
\]
On the compact interval in (30), the selected square root
has positive real part, so \(\Re u<1/2\). By decreasing
\(\delta\), we can have \(\Re B>3/4\) for the whole physical
arc. Thus every denominator in (37)--(38) is uniformly
separated from zero. In particular \(F_B\) and its inverse,
with any fixed number of \(t\)-derivatives, are uniformly
bounded.

The [corrected full Fourier packet](research_mixed_next_low_cardinal_full_fourier_packet.md),
Lemma 1, was derived from the initialized second-order column
recurrence and proves, uniformly on slightly enlarged compact
intervals,
\[
                \frac{v_{j-1}}{v_j}
                     =\rho(t_j)+N^{-1}\rho_1(t_j)+O(N^{-2}).
 \tag{39}
\]
This is a recurrence estimate; it does not differentiate an
unspecified \(O(N^{-1})\) packet error.

Set \(\epsilon=N^{-1}\) and
\[
 \begin{split}
 F_{B,1}(t)
    &=\frac{\{c(t)+h_B(t)F_B(t)\}\rho_1(t)
                        -h_B(t)\rho(t)F_B'(t)}
                       {1-h_B(t)\rho(t)},\\
 F_{B,\epsilon}(t)&=F_B(t)+\epsilon F_{B,1}(t).
 \end{split}
 \tag{40}
\]
All bounds just stated also hold for these functions. Define the
exact residual and exact error at physical rows in the compact
interval by
\[
 \begin{split}
 \varepsilon_{j,N}(B)
  &=v_j+c(t_j)v_{j-1}
       -\{F_{B,\epsilon}(t_j)v_j
            -h_B(t_j)F_{B,\epsilon}(t_j-\epsilon)v_{j-1}\},\\
 E_j(B)&=\kappa^2N^2a_j(B)+F_{B,\epsilon}(t_j)v_j .
 \end{split}
 \tag{41}
\]
Then (5) gives, exactly,
\[
 E_j(B)=h_B(t_j)E_{j-1}(B)-\varepsilon_{j,N}(B),\qquad
 \frac{E_j(B)}{H_{b,j}}-\frac{E_{j-1}(B)}{H_{b,j-1}}
                       =-\frac{\varepsilon_{j,N}(B)}{H_{b,j}}.
 \tag{42}
\]
Substitution of (39) in (41) shows
\[
                         |\varepsilon_{j,N}(B)|
                                  \le C N^{-2}|v_j|.
 \tag{43}
\]
Indeed the constant coefficient is (37), while the
\(\epsilon\) coefficient is
\[
 (c+h_BF_B)\rho_1-h_B\rho F_B'
                     -(1-h_B\rho)F_{B,1}=0 .
 \tag{44}
\]
The Taylor remainders are uniform for the whole fixed \(B\)-arc.
No freely chosen homogeneous constant occurs in (42).

## 6. The tilted profile pays both actual boundary terms

On the fixed interval \([l_0,r_0]\), define
\[
                      A_\theta(t)=A(t)-Q_\theta(t).
 \tag{45}
\]
Although \(J(\theta)\) need not have a bounded derivative at
zero, it is constant in \(t\). Hence \(Q_\theta'\) and
\(Q_\theta''\) tend uniformly to zero there as \(\theta\to0\).
Strict monotonicity of \(A\) away from \(x_*\) and its negative
second derivative near \(x_*\) imply, after another fixed
decrease of \(\delta\), that \(A_\theta\) has exactly one
critical point \(x_\theta\in(l,r)\). It is a nondegenerate
maximum, and \(x_\theta\to x_*\) uniformly as
\(\theta\le\delta\to0\).
We may also require
\[
            A(x_\theta)>\max\{A(l),A(r)\}.
 \tag{46}
\]
There is a uniform constant \(c_0>0\) such that
\[
 \begin{cases}
 A_\theta'(t)\ge c_0(x_\theta-t),&l_0\le t\le x_\theta,\\
 -A_\theta'(t)\ge c_0(t-x_\theta),&x_\theta\le t\le r_0 .
 \end{cases}
 \tag{47}
\]

Let \(w_{b,j}=|v_j/H_{b,j}|\). The compact factorial packet
applied only at \(t_j\) and \(t_j+\theta\), together with the
actual column packet, gives the following uniform ratio estimate:
\[
 \frac{w_{b,k}}{w_{b,j}}
       \le C\exp\!\left(N\{A_\theta(t_k)-A_\theta(t_j)\}\right),
                   \quad l_0\le t_j,t_k\le r_0 .
 \tag{48}
\]
The factor depending only on \(S_b\) cancels. More explicitly,
\[
 w_{b,j}
  =\frac{|\gamma_0|S_b|G(t_j)|}
            {2N\sqrt{\sin(\pi t_j)\sin(\pi(t_j+\theta))}}
       e^{N\{A(t_j)-J(t_j+\theta)+J(t_j)\}}
                                         (1+O(N^{-1})).
 \tag{49}
\]
All displayed \(t\)-dependent prefactors are uniformly positive
and smooth on the fixed interval. Formula (49) remains valid
at \(b=0\), since the use of the compact factorial packet
has not been extended to \(S_b\).

Integrating (47) and then summing a discrete Gaussian in (48)
yields
\[
 \begin{split}
 \sum_{l_0N\le k\le j} w_{b,k}
           &\le C\sqrt N\,w_{b,j},
                      &&l\le t_j\le x_\theta,\\
 \sum_{j<k\le r_0N} w_{b,k}
           &\le C\sqrt N\,w_{b,j},
                      &&x_\theta\le t_j\le r .
 \end{split}
 \tag{50}
\]
Rounding either fixed cut changes only the constant. For example,
on the left the exponent difference is bounded above by
\(-c_0(j-k)^2/(2N)\); the right calculation is the same.

It remains to pay the constants in the exact telescoper, not
just its residuals. Set \(j_-=\lfloor l_0N\rfloor\) and
\(j_+=\lceil r_0N\rceil\), using a slightly enlarged compact
interval in (39)--(49). Summing (32) from the genuine initial
value and from the genuine pre-reset anchor gives
\[
 \left|\frac{E_{j_-}(B)}{H_{b,j_-}}\right|
                   \le C N^C e^{NA(l_0+O(N^{-1}))},\qquad
 \left|\frac{E_{j_+}(B)}{H_{b,j_+}}\right|
                   \le C N^C e^{NA(r_0+O(N^{-1}))}.
 \tag{51}
\]
The left inequality uses \(|H|\ge1\) and the first two
conditions of (31); the right uses the same fact, (15)
and (29). The added \(F_{B,\epsilon}v\) terms obey those
same bounds. There is no factor \(e^{N\omega(\delta)}\)
in (51), since these constants are still divided by \(H\).

On the target interval the compact column lower bound and
(20) give
\[
 w_{b,j}\ge C^{-1}N^{-C}
                        e^{N\{A(t_j)-\omega(\delta)\}}.
 \tag{52}
\]
By (31) and (46), the appropriate constant in (51) is
exponentially smaller than (52): use the left constant for
\(t_j\le x_\theta\) and the right one for \(t_j\ge x_\theta\).
Thus both choices refer to actual boundary data and have a
uniform strict reserve.

Sum (42) from the corresponding cut. Equations (43), (50)
and (51)--(52) give the complete physical row asymptotic
\[
 \boxed{\quad
 a_j(r^b)=-\frac{v_j}{\kappa^2N^2}
          \left\{F_{r^b}(t_j)+N^{-1}F_{r^b,1}(t_j)
                                      +O(N^{-3/2})\right\},
 \quad l\le j/N\le r,\quad0\le b\le\delta N .
 \quad}
 \tag{53}
\]
The error is uniform in both physical indices and both parities.
The leading factor is bounded away from zero.
The tilted peak \(x_\theta\) was used only to choose the
direction in which to sum the error. The actual coefficient
profile in (53) is the original \(A\), with peak \(x_*\).

## 7. Full vectors and one common Fourier observation

Let \(\mathbf a_N(B)=(a_j(B))_{j=0}^{D}\).
Define comparison vectors, zero outside \(l\le t_j\le r\), by
\[
 p^{(2)}_{B,N,j}
       =-\frac{F_{B,\epsilon}(t_j)v_j}{\kappa^2N^2},
 \qquad
 p^{(0)}_{B,N,j}
       =-\frac{F_B(t_j)v_j}{\kappa^2N^2}.
 \tag{54}
\]
The uniform tails (34), row error (53), and the Gaussian norm
computation for the original column prove
\[
 \begin{split}
 \|\mathbf a_N(B)-p^{(2)}_{B,N}\|_2
                &\le C N^{-11/4}e^{NA_*},\\
 \|\mathbf a_N(B)-p^{(0)}_{B,N}\|_2
                &\le C N^{-1}\|p^{(0)}_{B,N}\|_2,\\
 \|\mathbf a_N(B)\|_2
   &=H_B\left(\frac{\pi}{\alpha}\right)^{1/4}
         N^{-5/4}e^{NA_*}(1+O(N^{-1/2})),\\
 H_B&=\frac{|F_B(x_*)G(x_*)|}{2\sin(\pi x_*)}.
 \end{split}
 \tag{55}
\]
All constants are uniform for the complete physical low-node
range, and \(H_B\) is uniformly positive. For the first line,
the relative interior error is \(O(N^{-3/2})\) and the simple
model norm is of order \(N^{-5/4}e^{NA_*}\); outside the
fixed interval (34) is exponentially smaller. The other lines
follow exactly as in the full first-node packet, with the
uniform smooth nonzero factor \(F_B\).

There is also a comparison in the original coefficient
coordinates. Put
\[
 R_B(t)=\frac{F_B(t)}{F_1(t)}
        =\frac{B(1-u(t))}{B-u(t)},\qquad
                       R_B^*=R_B(x_*).
 \tag{56}
\]
Here \(F_1\) denotes \(F_B\) at \(B=1\), not the correction
\(F_{B,1}\) in (40). Its nonzero values and fixed derivatives
are uniformly bounded. The Gaussian second moment and
\(|R_B(t)-R_B^*|\le C|t-x_*|\) imply
\[
       \|\mathbf a_N(B)-R_B^*\mathbf a_N(1)\|_2
                    \le C N^{-1/2}\|\mathbf a_N(1)\|_2 .
 \tag{57}
\]
This is an actual uniform approximation of the low-node
coefficient family by scalar multiples of one vector.

For a prescribed common phase, use the first-node phase on
the same fixed interval:
\[
 \sigma_{N,j}
    =-\frac{\gamma_0}{\kappa^2|\gamma_0|}
        \frac{F_1(t_j)G(t_j)}{|F_1(t_j)G(t_j)|}
                              e^{iN\Im I(t_j)},
 \tag{58}
\]
and set it to one outside. It is independent of the incoming
index \(b\). Define
\[
 \zeta_{B,N,j}
       =\frac{\sigma_{N,j}^{-1}a_j(B)}
                         {\|\mathbf a_N(B)\|_2},\qquad
 \widehat\zeta_{B,N}(m)
       =N^{-1/2}\sum_{j=0}^{D}\zeta_{B,N,j}e^{-2\pi imj/N}.
 \tag{59}
\]
For every fixed \(T<\infty\), the whole finite vector satisfies
\[
 \boxed{\quad
 \widehat\zeta_{B,N}(m)
   =\frac{R_B^*}{|R_B^*|}
      \left(\frac{4\pi}{\alpha}\right)^{1/4}
        N^{-1/4}e^{-2\pi imx_*}
             e^{-2\pi^2m^2/(\alpha N)}
                              (1+O_T(N^{-1/2})),
        \qquad |m|\le T\sqrt N .
 \quad}
 \tag{60}
\]
In particular the same prescribed zero mode is nonzero,
with modulus at least \(cN^{-1/4}\), for every low node.
For the cyclic shift \((\mathsf Sz)_j=z_{j-1\bmod N}\),
\[
           \|\mathsf S\zeta_{B,N}-\zeta_{B,N}\|_2
                         =\sqrt{\frac{\alpha}{2N}}+O(N^{-1}).
 \tag{61}
\]

To verify (60), after removing (58) the simple model is the
positive first-node Gaussian multiplied by the smooth complex
factor \(R_B(t)\). Its Taylor expansion near \(x_*\) has constant
term \(R_B^*\), with a uniform
\(O(N^{-1/2}(1+|s|))\) error on the Gaussian scale
\(s=(j-Nx_*)/\sqrt N\). The same Gaussian Riemann sum as in
the original Fourier theorem proves (60), including the phase
\(R_B^*/|R_B^*|\) after norm normalization. The complete actual
vector differs from this normalized model by \(O(N^{-1})\)
in \(\ell^2\), using (55) and the original column packet.
Its Fourier transform differs in each coefficient by at most
that amount, which is smaller than the allowed
\(O_T(N^{-3/4})\) absolute error in (60).

For (61), the additional smooth nonzero factor has an adjacent
ratio \(1+O(N^{-1})\). The leading adjacent ratio is still
\(1+\alpha s/\sqrt N+O((1+s^2)/N)\).
The squared Gaussian moment is therefore
\(\alpha/(2N)+O(N^{-3/2})\). Uniform tails and then the
\(O(N^{-1})\) vector error prove (61).
Both truncation boundaries and the cyclic seam have a strict
exponential reserve by (34).

## 8. Both exact sectors and the remaining signed observations

The unselected-sector coefficient in the same outgoing basis
is exactly
\[
 a_j^{(0)}(B)
       =\frac{B^{-j}p_j(B)}{P_bP_j}-a_j(B)
       =\begin{cases}
           H_{b,j}/P_b-a_j(B),&0\le j\le D-b,\\
           -a_j(B),&N-b\le j\le D .
         \end{cases}
 \tag{62}
\]
The second range is empty at \(b=0\). It records precisely
the terminating physical zeros, including the reset.
By (20) and the uniform factorial bound, the complete
homogeneous vector in (62) has exponential rate at most
\[
                    \omega(\delta)
                      +\sup_{\theta\le\delta}[-J(\theta)]
                                     \longrightarrow0 .
 \tag{63}
\]
Decrease the fixed \(\delta\) once more if necessary. This is
then strictly below \(A_*\), so (55)--(61) hold for the
unselected vector with the overall phase reversed. Both
sectors have a uniform, nonzero coefficient packet, even
though their sum is the small homogeneous vector (62).

For arbitrary weights \(w_b\), the exact finite sum of the
comparison (57) gives the useful bound
\[
 \left\|\sum_{b\le\delta N}w_b\mathbf a_N(r^b)
      -\mathbf a_N(1)\sum_{b\le\delta N}w_bR_{r^b}^*\right\|_2
       \le C N^{-1/2}\|\mathbf a_N(1)\|_2
                                      \sum_{b\le\delta N}|w_b|.
 \tag{64}
\]
This can be applied with the exact original prefactors and
ordinary-color coefficients in the low cardinal correction.
It does not give a relative error if the scalar sum on its
left cancels. The original ordinary normal adapters and
incoming coefficients have not been replaced by derivatives
of \(B\): all packet statements concern physical \(B=r^b\).

Finally, (60) is a Fourier transform in the coefficient index
\(j\). It is not the Newton evaluation (3), whose nonconstant
factorials and prescribed output remain. The proof supplies
neither noncancellation nor suppression of that complete
outgoing polynomial, nor of the remaining signed incoming
sum in the actual attachment. It does rule out a uniformly
polynomial bound on the separate coefficient vectors over
the entire fixed low-node interval, and it provides their
common actual leading vector and the explicit rational
incoming multiplier without losing either boundary forcing.
