# Endpoint connection constants and a finite-level bulk overlap

Private written proof, 16 November 2026.

The original microscopic endpoint values have explicit connection
constants. Their derivation uses the terminating endpoint recurrence,
an exact hypergeometric generating function, and a growing overlap
with the original finite-level recurrence. No interchange of a
fixed-index limit and a bulk limit is used.

The leading value oscillates in \(\log N\) at nonzero real endpoint
parameter. At parameter zero its two modes coalesce into a logarithm.
The theorem supplies the value-derived part of the actual normal
comparison; it does not identify a separately interpolated normal
with that derivative.

## 1. Original data and statement

Set
\[
 \theta=\pi/N,\quad s_r=2\sin(r\theta),\quad
 S_k=\prod_{r=1}^k s_r,\quad
 c(r)=2\cos((2r+1)\theta),\quad w_N(\alpha)=2\cosh(\alpha/N),
\]
\[
 e_k(Z)=S_k^{-2}\prod_{r<k}(c(r)-Z),\qquad
 K_N(Z,w)=\sum_{k=0}^{N-1}e_k(Z)e_k(w),\qquad
 F_{j,N}(\alpha)=K_N(c(j),w_N(\alpha)).
 \tag{1}
\]
These are ordinary original polynomials, including their high Newton
sector. Throughout the asymptotic theorem, \(\alpha\) is real and
\(|\alpha|\le A<\infty\). Put
\[
 \nu=\alpha/\pi,\qquad a=\tfrac12+i\nu/2,\qquad b=1-a,\qquad
 p=ab=\tfrac14(1+\nu^2).
 \tag{2}
\]
For real \(\nu\ne0\), define
\[
 k_\pm(\nu)=
       \frac{\Gamma(\pm i\nu)}
            {\Gamma(1/2\pm i\nu/2)^4},\qquad
 C_0(\nu)=k_++k_-,\qquad C_1(\nu)=i\nu(k_+-k_-).
 \tag{3}
\]
Both \(C_0,C_1\) have removable values at zero and are even analytic
functions on a complex neighborhood of any fixed compact real
\(\nu\)-interval. Their values there are
\[
 C_0(0)=\frac{2(\gamma_{\!E}+4\log2)}{\pi^2},\qquad
 C_1(0)=\frac2{\pi^2}.
 \tag{4}
\]
For \(s>0\), use the real logarithm in
\[
 g_\alpha(s)=\frac1s\left\{
 C_0(\nu)\cos(\nu\log s)
       +C_1(\nu)\frac{\sin(\nu\log s)}{\nu}\right\},\qquad
 S_N(x)=\frac{N}{\pi}\sin(\pi x).
 \tag{5}
\]
The sine quotient is interpreted by its value \(\log s\) at zero.
Equivalently, away from \(\nu=0\),
\[
             g_\alpha(s)=k_+s^{-1+i\nu}+k_-s^{-1-i\nu}.
 \tag{6}
\]

**Theorem.** Fix a closed interval \(I\Subset(0,1/2)\). There is
\(\epsilon>0\), depending only on \(A\) and a buffered choice of \(I\),
such that, uniformly at its physical nodes,
\[
 F_{j,N}(\alpha)=g_\alpha(S_N(j/N))+O(N^{-1-\epsilon}),
 \tag{7}
\]
\[
 N(F_{j,N}-F_{j-1,N})
       =\left.\partial_x g_\alpha(S_N(x))\right|_{x=j/N}
                                     +O(N^{-1-\epsilon}).
 \tag{8}
\]
The constants are uniform for real \(|\alpha|\le A\).

More generally, let \(f_N(x,\alpha)\) be any exact value interpolation
on a fixed larger bulk interval and a fixed complex \(x\)-neighborhood,
with a uniform polynomial analytic bound:
\[
 f_N(j/N,\alpha)=F_{j,N}(\alpha),\qquad |f_N|\le C N^P.
 \tag{9}
\]
For every fixed \(r\ge0\), on the smaller real interval,
\[
 \partial_x^r f_N(x,\alpha)
       =\partial_x^r g_\alpha(S_N(x))+O_r(N^{-1-\epsilon}),
 \tag{10}
\]
after reducing \(\epsilon\) once. No small-error assertion on a fixed
complex \(x\)-strip is made. The proof of (10) uses strips of width
comparable to \(1/\log N\).

The adopted two-channel theorem, as used in the pinned structural
source, supplies an interpolation satisfying (9). The conclusions
are independent of which such interpolation is chosen.

## 2. The universal endpoint recurrence and its generating function

At a physical index \(j\), the Newton sum (1) terminates at \(k=j\).
For each fixed \(j\), direct sine-product limits give
\[
 F_{j,N}(\alpha)\longrightarrow
 v_j(\alpha):=
 {}_4F_3\!\left(\begin{matrix}-j,j+1,a,b\\1,1,1\end{matrix};1\right)
 =\sum_{k=0}^j
       \frac{(-j)_k(j+1)_k(a)_k(b)_k}{(k!)^4}.
 \tag{11}
\]
Indeed
\[
 e_k(c(j))\longrightarrow
       \frac{(-1)^k(-j)_k(j+1)_k}{(k!)^2},\qquad
 e_k(w_N(\alpha))\longrightarrow
       \frac{(-1)^k(a)_k(b)_k}{(k!)^2}.
 \]
Only a fixed finite sum is involved in (11).

The exact original recurrence is
\[
 F_{j+1,N}=(1+d_{j,N})F_{j,N}
                         +q_{j,N}(F_{j,N}-F_{j-1,N}),
\]
\[
 q_{j,N}=\frac{C_N(j)}{A_N(j)},\qquad
 d_{j,N}=\frac{c(0)-w_N(\alpha)}{A_N(j)},\qquad
 A_N(j)=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\quad
 C_N(j)=\frac{s_j^4}{s_{2j}s_{2j+1}}.
 \tag{12}
\]
At zero use \(C_N(0)=0\). Its fixed-index limits are
\[
 q_j^0=\frac{j^3}{(j+1)^3},\qquad
 d_j^0=-\frac{2p(2j+1)}{(j+1)^3}.
 \tag{13}
\]
Thus
\[
 (j+1)^3v_{j+1}
 =\{(j+1)^3+j^3-2p(2j+1)\}v_j-j^3v_{j-1},
 \quad v_0=1,\quad v_1=1-2p.
 \tag{14}
\]
This conclusion could also be obtained directly from the terminating
sum, but (12) fixes its original normalization.

The generating identity needed for the connection problem is
\[
 \boxed{\quad
 V(z):=\sum_{j\ge0}v_j z^j
 ={}_2F_1(a,a;1;z)\,{}_2F_1(b,b;1;z)
 =(1-z)^{2a-1}{}_2F_1(a,a;1;z)^2 .
 \quad}
 \tag{15}
\]
Here all functions start with their analytic branches at \(z=0\).
We verify the identity rather than invoke an identification of
orthogonal polynomials.

Write \(D=z\partial_z\). Equation (14) is equivalent to
\[
 [D^3-z\{2D^3+3D^2+(3-4p)D+1-2p\}
                         +z^2(D+1)^3]V=0.
 \tag{16}
\]
For example, the left shift contributes \(D^3V\), and the last
shift contributes \(z^2(D+1)^3V\). Conversely its coefficient
recurrence determines every analytic coefficient from \(v_0\).

For an explicit check of the proposed right side, let
\(k=a-1/2\), \(f={}_2F_1(a,a;1;z)\), and
\(h=(1-z)^k f\). The hypergeometric equation gives
\[
 z(1-z)h''+(1-2z)h'
              -\left\{\tfrac14+\frac{k^2}{1-z}\right\}h=0.
 \tag{17}
\]
If \(h''+Ph'+Qh=0\), direct differentiation of \(h^2\) gives
\[
 (h^2)'''+3P(h^2)''
 +(P'+4Q+2P^2)(h^2)'
 +(2Q'+4PQ)h^2=0.
 \tag{18}
\]
In (17),
\[
 P=\frac{1-2z}{z(1-z)},\qquad
 Q=-\frac1{4z(1-z)}-\frac{k^2}{z(1-z)^2}.
 \]
Multiplying (18) by \(z^3(1-z)^2\) yields coefficients
\[
 \begin{array}{c|c}
 \partial_z^3&z^3(1-z)^2\\
 \partial_z^2&3z^2(1-z)(1-2z)\\
 \partial_z&z+(4p-8)z^2+7z^3\\
 1&-(1-2p)z+z^2
 \end{array}
 \]
because \(p=1/4-k^2\). These are exactly (16) in ordinary
derivatives. The constant coefficient is one. Uniqueness of its
analytic coefficient recurrence proves the final expression in
(15). The middle expression follows from Euler's transformation
\({}_2F_1(b,b;1;z)=(1-z)^{2a-1}{}_2F_1(a,a;1;z)\);
alternatively the same substitution into the second-order equation,
with its value and derivative at zero, proves that transformation.

## 3. Connection constants, coefficient bounds, and coalescence

Put \(\zeta=1-z\). Away from \(\nu=0\), in a small slit
neighborhood of \(z=1\), the connection formula is
\[
 {}_2F_1(a,a;1;z)
   =A_\nu\,{}_2F_1(a,a;2a;\zeta)
    +B_\nu\,\zeta^{-i\nu}{}_2F_1(b,b;2b;\zeta),
\]
\[
 A_\nu=\frac{\Gamma(-i\nu)}{\Gamma(b)^2},\qquad
 B_\nu=\frac{\Gamma(i\nu)}{\Gamma(a)^2}.
 \tag{19}
\]
Here is a direct normalization argument for these constants.
For \(0<\Re a<1\), Euler's integral gives
\[
 {}_2F_1(a,a;1;z)=
 \frac1{\Gamma(a)\Gamma(1-a)}
 \int_0^1u^{a-1}(1-u)^{-a}(1-zu)^{-a}\,du.
 \tag{20}
\]
Its expansion at zero proves the integral by the beta integral.
The two functions in (19) solve the same differential equation
and have distinct local exponents when \(2a-1\ne0\) is not an
integer. For \(\Re a<1/2\), evaluation of (20) at \(z=1\)
is another beta integral and gives
\(\Gamma(1-2a)/\Gamma(1-a)^2\) for the regular coefficient.
For \(\Re a>1/2\), rescaling \(1-u=(1-z)v\) in its singular
part gives
\(\Gamma(2a-1)/\Gamma(a)^2\) for the singular coefficient.
These coefficients are meromorphic in \(a\). Analytic continuation
of the two local solutions and their Wronskian proves (19) throughout
a neighborhood of the compact real \(\nu\)-interval, except its
displayed removable coalescence. This argument also fixes the
branches inherited from \(z=0\).

Substitution in (15) shows that its only leading nonanalytic terms
at one are
\[
        A_\nu^2(1-z)^{i\nu}
                   +B_\nu^2(1-z)^{-i\nu}.
 \tag{21}
\]
The cross term is analytic at one. Both analytic multipliers in
(19) have value one there.

We give the uniform coefficient estimate used below. Choose a small
fixed \(0<\sigma<1/4\). Uniformly for \(\nu\) on a fixed compact
real interval,
\[
 v_j=g_\alpha(j)+O_A(j^{-2+\sigma}),\qquad
 v_j-v_{j-1}
   =g_\alpha(j)-g_\alpha(j-1)+O_A(j^{-3+\sigma}).
 \tag{22}
\]
To justify the coefficient transfer first away from zero, recall
the exact identity
\[
 [z^j](1-z)^\lambda
   =\frac{\Gamma(j-\lambda)}
          {\Gamma(-\lambda)\Gamma(j+1)}.
 \tag{23}
\]
For \(\lambda\) in compact subsets with \(\Re\lambda>-1\),
the beta integral for the ratio of gamma functions, followed by
the substitution \(v=j(1-u)\), gives
\[
 \frac{\Gamma(j-\lambda)}{\Gamma(j+1)}
            =j^{-1-\lambda}\{1+O(j^{-1})\}.
 \tag{24}
\]
The bound is uniform on those compact sets; splitting the integral
at \(v=j^{1/3}\), Taylor expansion on the first part and its
exponential tail proves the stated error. Analytic continuation
interprets (23) at its removable integer parameters.

For clarity, the local remainder transfer needs no global
convergence of the series at one. After subtracting (21) and the
constant cross term, the remainder is
\(O(|1-z|^{1-\sigma})\), uniformly on a compact parameter set
with \(|\Im\nu|<\sigma\) avoiding zero. It is analytic in a disk
larger than the unit disk slit along \([1,\infty)\).
Deform the coefficient contour to a circle of radius \(1/j\)
about one and two fixed-angle rays \(1+t e^{\pm i\varphi}\),
\(0<\varphi<\pi/2\), followed by fixed outer arcs.
On those rays \(|z|^{-j-1}\le C e^{-cjt}\).
The small circle and
\(\int_{1/j}^{r}t^{1-\sigma}e^{-cjt}\,dt\)
are both \(O(j^{-2+\sigma})\); the outer arcs are exponentially
small. Multiplication by \(1-z\) gives
\(O(j^{-3+\sigma})\) for the coefficient difference.
Together with (23)--(24), this proves (22) away from zero.
The same argument for the explicit leading powers gives their
first-difference accuracy as stated.

For uniformity at zero, use a fixed small parameter circle
\(|\nu|=\sigma/2\). The expressions
\[
 k_+j^{-1+i\nu}+k_-j^{-1-i\nu},\qquad
 k_++k_-,\qquad i\nu(k_+-k_-)
 \]
have removable singularities at \(\nu=0\).
Both the exact coefficients and their differences are holomorphic
inside this circle. The estimates just proved on its boundary,
with an exponent smaller than the chosen \(\sigma\), extend to
the disk by the maximum principle. A finite compact cover treats
the remaining real parameters and proves (22).

Finally the expansions
\(\Gamma(z)=z^{-1}-\gamma_{\!E}+O(z)\) and
\(\psi(1/2)=-\gamma_{\!E}-2\log2\), the latter following from
the gamma duplication identity, give (4). In particular
\[
 g_0(s)=\frac{2}{\pi^2s}
                        \{\log s+\gamma_{\!E}+4\log2\}.
 \tag{25}
\]
The coalescence is part of one uniform real-parameter estimate,
not a limit taken after \(j\) or \(N\).

## 4. A growing finite-level endpoint overlap

For \(j\ge1\), use the balanced state
\[
 Z_{j,N}=
   \binom{jF_{j,N}}{j^2(F_{j,N}-F_{j-1,N})}.
 \tag{26}
\]
Equation (12) gives the exact transfer
\[
 Z_{j+1,N}=M_{j,N}Z_{j,N},\qquad
 M_{j,N}=
 \begin{pmatrix}
 (j+1)(1+d_{j,N})/j&(j+1)q_{j,N}/j^2\\
 (j+1)^2d_{j,N}/j&(j+1)^2q_{j,N}/j^2
 \end{pmatrix}.
 \tag{27}
\]
Let \(M_j^0\) be the matrix with the limiting coefficients (13);
it transports \(Z_j^0=(jv_j,j^2(v_j-v_{j-1}))^t\).

Uniformly for \(1\le j\le J=o(N)\), the exact sine quotients imply
\[
 q_{j,N}-q_j^0=O_A(j/N^2),\qquad
 d_{j,N}-d_j^0=O_A(N^{-2}),\qquad
 M_{j,N}-M_j^0=O_A(j/N^2).
 \tag{28}
\]
For the first estimate, the exact quotient is
\[
 q_{j,N}=
 \left(\frac{\sin(j\pi/N)}{\sin((j+1)\pi/N)}\right)^4
       \frac{\sin((2j+2)\pi/N)}{\sin(2j\pi/N)}.
 \]
After extracting \(q_j^0\), the logarithms of the remaining sinc
quotients are differences over intervals of length \(O(N^{-1})\).
Since \((\log\operatorname{sinc})'(u)=O(u)\) near zero, their
total is \(O(j/N^2)\). For \(d\), the relative error of its
sine denominator is \(O((j+1)^2/N^2)\), whereas \(d_j^0=O_A(j^{-2})\);
the numerator has relative error \(O_A(N^{-2})\).
This proves (28), also for the finitely many initial indices.

There is a constant \(B_A\ge1\) such that, throughout this range
for sufficiently large \(N\),
\[
 \|M_j^0\|,\ \|M_{j,N}\|\le1+B_A/j,\qquad
 \left\|\prod_{r=k}^{j-1}M_{r,N}\right\|
                                      \le C_A(j/k)^{B_A}.
 \tag{29}
\]
Indeed the limiting expansion is
\[
 M_j^0=I+\frac1j
       \begin{pmatrix}1&1\\-(1+\nu^2)&-1\end{pmatrix}
                     +O_A(j^{-2}),
 \]
and (28) is absorbed into \(C_A/j\) when \(j=o(N)\).
Increase \(B_A\) to cover the initial indices.

The initial vector at \(j=1\) differs by \(O_A(N^{-2})\) from
its limiting vector, directly from (12). Equation (22) gives
\(\|Z_j^0\|\le C_A(1+\log(j+1))\) for real parameters.
Variation of constants in (27), using (28)--(29), therefore gives
the deliberately conservative estimate
\[
 \|Z_{J,N}-Z_J^0\|
       \le C_A N^{-2}J^{B_A+2}(1+\log J).
 \tag{30}
\]
For example, bound each summand by
\(C_A(J/k)^{B_A}(k/N^2)(1+\log k)\) and sum;
the displayed bound is larger and valid for every \(B_A\ge1\).

Fix once and for all
\[
 0<\kappa<\frac1{4(B_A+3)},\qquad J=\lfloor N^\kappa\rfloor.
 \tag{31}
\]
Then (30) tends to zero much faster than \(J^{-1+\sigma}\).
Combining it with (22) yields the actual growing-overlap estimate
\[
 Z_{J,N}=
 \binom{Jg_\alpha(J)}
 {J^2\{g_\alpha(J)-g_\alpha(J-1)\}}
                         +O_A(J^{-1+\sigma}).
 \tag{32}
\]
All comparisons have used the exact finite recurrence up to \(J\).
This is the step that prevents an exchange of nonuniform limits.

## 5. Transport from the overlap to a fixed bulk interval

Choose \(0<b_*<1/2\) larger than the bulk intervals to be used.
For real \(x\in(0,b_*]\), set
\[
 y_{0,N}(x)=S_N(x)^{-1}\cos(\nu\log S_N(x)),\qquad
 y_{1,N}(x)=S_N(x)^{-1}
                    \frac{\sin(\nu\log S_N(x))}{\nu}.
 \tag{33}
\]
Their linear combination with coefficients \(C_0,C_1\) is
\(g_\alpha(S_N(x))\). Multiplying the coalescence-safe Euler modes
in the pinned source by constant factors and taking linear
combinations shows, or direct differentiation verifies, that both
solve
\[
 y''+\pi(3\cot\pi x+\tan\pi x)y'
                         +(\pi^2+\alpha^2)\cot^2(\pi x)y=0.
 \tag{34}
\]
Their Wronskian in \(x\) is
\[
       y_{0,N}y_{1,N}'-y_{1,N}y_{0,N}'
                  =\frac{N\cos(\pi x)}{S_N(x)^3}.
 \tag{35}
\]

Form their sampled balanced matrix
\[
 \Psi_{j,N}=
 \begin{pmatrix}
 j y_{0,N}(j/N)&j y_{1,N}(j/N)\\
 j^2[y_{0,N}(j/N)-y_{0,N}((j-1)/N)]&
 j^2[y_{1,N}(j/N)-y_{1,N}((j-1)/N)]
 \end{pmatrix}.
 \tag{36}
\]
Uniformly for \(J\le j\le b_*N\),
\[
 \|\Psi_{j,N}\|+\|\Psi_{j,N}^{-1}\|
                                     \le C_A(1+\log N),
 \tag{37}
\]
for sufficiently large \(N\). To check the inverse, Taylor's
formula in the unscaled index gives
\[
 \det\Psi_{j,N}
   =\frac{j^3\cos(\pi j/N)}{S_N(j/N)^3}
                       +O_A((1+\log N)^2/j).
 \tag{38}
\]
The leading term is bounded above and below by positive constants
on this range. The error tends to zero because \(J=N^\kappa+O(1)\).
The entry bounds follow from \(S_N(j/N)\asymp j\) and (33).
This proves (37), including \(\nu=0\).

The sampled columns are approximate solutions of the exact recurrence:
\[
 \|\Psi_{j+1,N}-M_{j,N}\Psi_{j,N}\|
                      \le C_A(1+\log N)/j^2.
 \tag{39}
\]
Here is an estimate retaining the singular endpoint scale.
Regard a column \(y(j/N)\) as a function of \(j\).
Its first four index derivatives have bounds
\[
             C_A(1+\log N)j^{-1-r},\qquad 0\le r\le4.
 \tag{40}
\]
The exact quotients satisfy, for \(J\le j\le b_*N\),
\[
 q_{j,N}=1-P_j+O_A(j^{-2}),\qquad
 d_{j,N}=-Q_j+O_A(j^{-3}),
 \]
\[
 P_j=\frac{\pi}{N}(3\cot(\pi j/N)+\tan(\pi j/N)),\qquad
 Q_j=\frac{\pi^2+\alpha^2}{N^2}\cot^2(\pi j/N).
 \tag{41}
\]
Taylor expansion of the sine quotients proves these bounds uniformly:
their logarithmic derivatives cost \(O(1/j)\), with the next
derivatives \(O(1/j^2)\). The numerator in \(d\) has error
\(O_A(N^{-4})\), while its denominator has relative error
\(O(1/j)\) from \(\tan^2(\pi j/N)\).

Expanding the scalar residual from (12), its leading part is
\(y_{jj}+P_jy_j+Q_jy\), zero by (34).
Equations (40)--(41) bound the residual by
\(C_A(1+\log N)j^{-4}\).
The two balanced residual entries multiply that scalar residual
by \(j+1\) and \((j+1)^2\), respectively. This proves (39).

Write \(Z_{j,N}=\Psi_{j,N}a_{j,N}\). Its exact coefficient transfer
is
\[
 a_{j+1,N}=\{I+R_{j,N}\}a_{j,N},\qquad
                   \|R_{j,N}\|\le C_A(1+\log N)^2/j^2.
 \tag{42}
\]
Thus
\[
 \sum_{j=J}^{\lfloor b_*N\rfloor}\|R_{j,N}\|
                  \le C_A(1+\log N)^2/J=o(1).
 \tag{43}
\]
At the overlap, \(S_N(J/N)=J\{1+O(J^2/N^2)\}\). Using this
and its first index difference in (32)--(33), then (37), gives
\[
 a_{J,N}=
       \binom{C_0(\nu)}{C_1(\nu)}
          +O_A((1+\log N)^2J^{-1+\sigma}).
 \tag{44}
\]
The \(J^2/N^2\) error and (30) are smaller by (31).
The elementary product bound
\(\prod(1+\|R_j\|)\le\exp(\sum\|R_j\|)\)
and (43) now show that (44), with another fixed logarithmic power,
holds for every \(J\le j\le b_*N\).

On a fixed bulk interval, both balanced entries are converted back
to \(F\) and \(N\Delta F\) with a factor \(O(N^{-1})\).
Consequently the errors are at most
\[
              C_A N^{-1}(1+\log N)^M J^{-1+\sigma}
 \tag{45}
\]
for an absolute finite power \(M\) in this proof.
Replacing the sampled first difference of (33) by its \(x\)-derivative
costs only \(O_A(N^{-2}(1+\log N))\) on that interval.
For example any \(\epsilon<\kappa/2\), reduced if necessary, is
valid in (7)--(8), because \(\sigma<1/4\).
This proves the first part of the theorem with an explicit permitted
choice of overlap exponent (31).

## 6. Derivatives of the actual moderate value interpolation

We record the elementary interpolation principle used here.
Suppose \(r_N\) is holomorphic and polynomially bounded on a fixed
complex neighborhood of a real interval \(I_2\). Suppose its values
on the spacing-\(N^{-1}\) grid obey
\[
                  |r_N(j/N)|\le\varepsilon_N
                       \quad(j/N\in I_2),
 \tag{46}
\]
where \(\varepsilon_N\) is bounded below by some negative power
of \(N\). On any buffered interval \(I_1\), interpolation at a
fixed number \(M+1\) of neighboring grid nodes gives
\[
           |r_N(x)|\le C_M\varepsilon_N+O(N^{P-M-1})
                         \qquad(x\in I_1).
 \tag{47}
\]
The Lagrange coefficients are bounded since all spacings are
\(N^{-1}\) and the interpolation point is within a fixed number
of spacings of those nodes. Cauchy's formula bounds the derivative
in the usual interpolation remainder by \(C_MN^P\) on a fixed
larger neighborhood; its product of spacings is \(O_M(N^{-M-1})\).
Choose a fixed \(M\) making that error smaller than (46).

This real bound extends with only a constant factor to a shrinking
strip
\[
       x\in I_0,\qquad |\Im x|\le c/\log N,\qquad
                         I_0\Subset\operatorname{int}I_1.
 \tag{48}
\]
Indeed apply the two-constants theorem to upper and lower fixed
rectangles based on \(I_1\). On their real base use (47); on all
other sides use \(CN^P\). At points over \(I_0\), the harmonic
measure of the other sides is at most \(C|\Im x|\): this follows
from the bounded normal derivative of that fixed harmonic function
on a buffered segment of the straight base. Hence its contribution
to the logarithm of the bound is at most \(C|\Im x|\log N\).
Equation (48) makes it bounded. Cauchy's formula on disks of radius
\(c/(2\log N)\) then gives
\[
       |\partial_x^r r_N(x)|\le C_r(\log N)^r\varepsilon_N
                             \qquad(x\in I_0).
 \tag{49}
\]
The same reasoning works if a harmless fixed logarithmic power
is included in \(\varepsilon_N\).

Apply this principle to
\[
                    r_N(x,\alpha)=f_N(x,\alpha)
                                       -g_\alpha(S_N(x)).
 \]
The second function is holomorphic and polynomially bounded on a
fixed buffered bulk strip: choose the branch of \(\log\sin\pi x\)
real on the real interval. Its bound for real compact \(\alpha\)
is \(O_A((1+\log N)/N)\) on that strip.
The first has its hypothesized bound (9).
Equation (7), proved on a slightly larger interval, supplies (46).
All constants in (47)--(49) are uniform in the real parameter.
Absorb the fixed logarithmic factors into a smaller positive
\(\epsilon\). This proves (10) for every fixed derivative order,
without asserting a fixed-strip small-error estimate.

## 7. Source placement and limits of the conclusion

At zero parameter, the explicit leading value is
\[
 \frac{2}{\pi N\sin(\pi x)}
       \left\{\log\!\left(\frac{N\sin(\pi x)}{\pi}\right)
                                +\gamma_{\!E}+4\log2\right\}.
 \tag{50}
\]
For real nonzero parameter \(k_-=\overline{k_+}\), so (6) is an
oscillatory real expression. This theorem asserts an additive
power-saving error, not a relative error or a nonzero scalar unit.

Let \(G_{j,N}=\partial_ZK_N(c(j),w_N(\alpha))\) be the original
spectral normal and \(f_N\) any interpolation (9). Its true defect is
\[
                   \Delta_j=Nc'(j)G_{j,N}-\partial_x f_N(j/N).
 \]
The proved value matching therefore gives the actual subtraction
term in that source equation:
\[
 \Delta_j=Nc'(j)G_{j,N}
       -\left.\partial_xg_\alpha(S_N(x))\right|_{x=j/N}
                                    +O(N^{-1-\epsilon}).
 \tag{51}
\]
No common-index coefficient derivative is substituted for
\(\partial_x f_N\). Equation (51) does not set \(\Delta_j\) to zero.
If a separately proved scalar-compatibility theorem controls that
defect, it can be combined with (51) to obtain the actual normal
asymptotic. The two-ended endpoint normal and its propagated source
are not dropped merely because (11) is terminating.

All external index endpoints, odd simple-node closing, full trace
currents, and other graph spectators remain outside this buffered
value asymptotic. No filled-action estimate, original cycle
coefficient, or noncancellation of the whole source follows.

## 8. Coverage and direct source

A search of the endpoint and physical-row notes found the exact
finite recurrence, moderate value interpolation and Euler modes,
but not their universal generating connection or a growing endpoint
overlap. The complete direct source was read at its unchanged pin,
with all used implications and the hash checked:

* [Original two-mode transport and exact finite recurrence](research_endpoint_normal_defect_two_mode_transport.md),
  SHA256 91620d1ea26793157843f78fff32c7d3eca62509799114a2d3069af8b96b47dc:
  the original kernel, recurrence, coalescence-safe Euler modes,
  existence and meaning of moderate value interpolation, and the
  distinction between that derivative and the actual normal.

The generating identity, beta connection, uniform coefficient
transfer, growing overlap and derivative bridge are proved here.
Only written proofs, text reads and hashes were used. No mathematical
program, numerical experiment, test or build was run. Adopted notes
and public manuscripts are unchanged.
