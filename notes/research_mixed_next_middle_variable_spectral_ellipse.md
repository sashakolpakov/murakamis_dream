# Variable spectral ellipses for the exact outgoing coefficients

Private written source proof, 8 November 2026. The original outgoing
polynomial has a product-degree estimate on every fixed spectral
ellipse. Optimizing the ellipse height gives a stronger decay bound
for its actual Chebyshev coefficients. The complete outgoing finite
source is retained throughout.

This does not estimate the remaining outer radical observation.
No mathematical numerical evaluation, saved-value calculation, or
change to a frozen proof is used.

## 1. Exact source and statements

Use the actual complete reference of
[the weighted outgoing theorem](research_mixed_next_middle_weighted_outgoing_kernel.md):
words in powers three and four beginning \(343\), of length at least
five, at their original complete outside values. In particular,
\[
 Z_*=e^{-2\pi iz_*},\qquad
 3/10\le\Re z_*\le39/100,\qquad 4/5<|Z_*|<8/7,
\]
\[
 -3/100<h_t,\Im z_*<1/50,\qquad
 \Lambda=\Re\mathcal P_*>419/200,\qquad
 E_*=\Lambda-\frac{2383}{1500}-\frac1{50}
       >\frac{1459}{3000}.
 \tag{1}
\]
No independent substitution for the actual reference is made.
Keep
\[
\begin{gathered}
 q=e^{\pi i/N},\quad r=q^{-2},\quad D=N-1,\quad
 M=\lceil N/2\rceil,\quad U=D-M=\lfloor N/2\rfloor-1,\\
 L=\lfloor N/6\rfloor,\quad d=U-L<N/3,\quad
 K=\lfloor N/4096\rfloor,\quad Y_N=r^M,\\
 s_n=2\sin(\pi n/N),\quad c_n=2\cos((2n+1)\pi/N),\\
 P_k=(r;r)_k,\qquad p_k(Z)=(rZ;r)_k .
\end{gathered} \tag{2}
\]
The letter \(d\) denotes a degree, not the forced factorial polynomial.
All statements concern sufficiently large levels of both parities.

The exact products from
[the all-Casimir amplitude theorem](research_mixed_next_middle_casimir_polynomial_amplitude.md)
are
\[
 \widehat P_{\ell,N}(\xi,T)=
 \prod_{n=U-\ell+1}^{U}
        q\,\frac{(\xi-c_n)(q^n-Tq^{-n})}{i s_n^3},
 \qquad 0\le\ell\le d .
 \tag{3}
\]
The empty product is one. Define their two outgoing observations
\[
\begin{split}
 B_{\ell,N}^{\rm all}(\xi)
  &=\sum_{k=0}^{U}
       \frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}
                   \widehat P_{\ell,N}(\xi,e^{2\pi ik/N}),\\
 B_{\ell,N}^{>}(\xi)
  &=\sum_{k=K+1}^{U}
       \frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}
                   \widehat P_{\ell,N}(\xi,e^{2\pi ik/N}),\\
 H_N^{\rm all}(\xi)&=\sum_{\ell=0}^{d}B_{\ell,N}^{\rm all}(\xi),
 \qquad H_N(\xi)=\sum_{\ell=0}^{d}B_{\ell,N}^{>}(\xi).
\end{split} \tag{4}
\]
Each \(B_{\ell,N}\) is a polynomial of degree at most \(\ell\).
These are the same exact polynomials as in
[the fixed-ellipse theorem](research_mixed_next_middle_fixed_spectral_ellipse.md);
in particular no product tail or endpoint amplitude is replaced.

For \(h\ge0\), let \(\mathcal E_h\) be the filled ellipse with boundary
\(\xi=2\cos(\theta+ih)\). At \(h=0\) this means \([-2,2]\).
Set
\[
 a=\frac3{20},\qquad
 c=\frac{3\sqrt3}{2\pi},\qquad
 \lambda=-\log\cos(\pi a),\qquad
 g(h)=c(\cosh h-1)-\lambda .
 \tag{5}
\]

**Theorem 1.** For every fixed \(H_{\max}<\infty\) and \(\tau>0\),
there are constants independent of \(h,\ell,N\) such that
\[
 \sup_{\xi\in\mathcal E_h}
 \bigl(|B_{\ell,N}^{\rm all}(\xi)|+
                    |B_{\ell,N}^{>}(\xi)|\bigr)
 \le C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
            e^{N(E_*+\tau)+\ell g(h)},
 \quad 0\le h\le H_{\max},\quad0\le\ell\le d .
 \tag{6}
\]
Consequently,
\[
 \sup_{\mathcal E_h}(|H_N^{\rm all}|+|H_N|)
 \le C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
             e^{N(E_*+\tau)+d\,g(h)_+}.
 \tag{7}
\]

For either polynomial, write its exact Chebyshev expansion as
\[
 H(\xi)=\sum_{b=0}^{d}h_{b,N}T_b(\xi/2).
 \tag{8}
\]
The constants below include the different normalization of \(b=0\).
Theorem 1 implies, for every \(0\le h\le H_{\max}\),
\[
 |h_{b,N}|
 \le C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
   \exp\!\left\{N(E_*+\tau)-hb+
                \max_{b\le\ell\le d}\ell g(h)\right\}.
 \tag{9}
\]
The maximum over product degrees is essential; it is not replaced
by the value of the coherent sum.

Here is an explicit optimized version of (9). Define
\[
 h_0=\operatorname{arcosh}(1+\lambda/c),\qquad
 \rho_0=c\sinh h_0=\sqrt{2c\lambda+\lambda^2},
 \tag{10}
\]
and, for \(0\le\rho\le1\), define
\[
 I(\rho)=
 \begin{cases}
 h_0\rho,&0\le\rho\le\rho_0,\\[2mm]
 \rho\,\operatorname{arsinh}(\rho/c)
       -\sqrt{c^2+\rho^2}+c+\lambda,
       &\rho_0\le\rho\le1 .
 \end{cases}
 \tag{11}
\]

**Theorem 2.** For both exact polynomials in (4), every \(\tau>0\),
and \(0\le b\le d\),
\[
 \boxed{\quad
 |h_{b,N}|\le C_\tau N^{A_\tau}
              \exp\{N(E_*+\tau)-d\,I(b/d)\}.
 \quad} \tag{12}
\]
All heights used to prove (12) lie in the fixed interval
\([0,\log3]\). Moreover,
\[
 h_0>\frac12+\frac1{300}>\frac{201}{400},\qquad
 I(\rho)\ge h_0\rho,
 \tag{13}
\]
with strict inequality in the second assertion when \(\rho>\rho_0\).
Thus this improves the previously proved coefficient factor
\(\exp(-201b/400)\), and gives additional decay for large \(b/d\).

## 2. The product-degree estimate on a variable ellipse

We retain two potential estimates proved in Sections 2--3 of the
fixed-ellipse theorem. Write
\[
 J(x)=\int_0^x\log|2\sin\pi s|\,ds,\qquad
 K_T(x)=\int_x^{1/2}
       \log\frac{|1-Te^{-2\pi is}|}{2\sin\pi s}\,ds .
 \tag{14}
\]
For \(1/6\le x\le1/2\), \(T=R e^{2\pi iv}\), \(0\le R\le1\),
and \(a\le v\le1/2\), that proof gives
\[
 K_T(x)\le(1/2-x)\log\cos(\pi a)=-\lambda(1/2-x).
 \tag{15}
\]
This is an integrated potential comparison, including the radial
endpoints and movable zeros. Its angular maximum is at \(v=a\)
or \(1/2\); the radial maximum at those endpoints is at \(R=0\)
or \(1\). No pointwise radial monotonicity is being assumed.
For \(R=1\), \(0\le v\le a\), the same proof instead gives
\[
 K_{e^{2\pi iv}}(x)
       \le(1/2-x)\log\cos(\pi v).
 \tag{16}
\]

The spectral part of that proof was not restricted to height \(1/2\).
For every boundary point of \(\mathcal E_h\), it gives
\[
 \int_x^{1/2}
   \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
 \le \frac{\cosh h-1}{2\pi}\cot(\pi x)
 \le c(\cosh h-1)(1/2-x).
 \tag{17}
\]
The first comparison follows by angular monotonicity of the
integrated cosine potential, whose largest tail is at
\(\xi=2\cosh h\), and then \(\log(1+t)\le t\).
The second uses
\(\cot(\pi x)/(1/2-x)\le3\sqrt3\).
Both assertions extend to \(h=0\) by integrated-log continuity.

Put \(x=(U-\ell)/N\). The exact zero-safe mesh estimate is
\[
 \log|\widehat P_{\ell,N}(\xi,T)|
 \le N\left\{
   \int_x^{1/2}
      \log\frac{|\xi-2\cos(2\pi s)|}{4\sin^2(\pi s)}\,ds
                      +K_T(x)\right\}+C_{H_{\max}}\log N.
 \tag{18}
\]
It holds uniformly for \(0\le h\le H_{\max}\), on the ellipse
boundary and on the compact upper unit outgoing sector.
To recall why zeros cause no failure, factor the numerators into
circle logarithms. Outside a closest mesh cell to each zero,
the integrated derivative errors sum to \(O(\log N)\). Rescaling
the closest cell gives the same one-sided upper error; an exact
sampled zero only decreases the left side. The denominators are
regular for \(L/N\le s\le1/2\). On a bounded height range the
same estimates are uniform, including colliding real numerator
zeros at the spectral endpoints.

The shift in \(c_n\), the exact value of \(U\), and the possible
sliver \(L/N<1/6\) change (18) by at most another \(C\log N\).
Also \(N(1/2-x)-\ell=N/2-U\) is either \(1\) or \(3/2\).
Multiplying this bounded discrepancy by \(g(h)\) costs a uniform
constant on a bounded height range, regardless of the sign of
\(g(h)\). Equations (15),(17),(18) prove
\[
 |\widehat P_{\ell,N}(\xi,T)|
       \le C N^A e^{\ell g(h)},
 \qquad \xi\in\mathcal E_h,\quad
 T=R e^{2\pi iv},\quad R\le1,\ a\le v\le1/2 .
 \tag{19}
\]
Maximum modulus in the spectral polynomial supplies the filled
ellipse before any products are summed.

Every outgoing zero of each exact product is on the unit circle.
For the same complex spectral point, including when its coefficient
vanishes, the exact identity is
\[
 |\widehat P_{\ell,N}(\xi,T)|
   =|T|^\ell
       |\widehat P_{\ell,N}(\xi,1/\overline T)|.
 \tag{20}
\]
This reflection preserves the outgoing angular sector. Thus (19)
implies the all-height bound
\[
 |\widehat P_{\ell,N}(\xi,e^{2\pi i(v+iy)})|
 \le C N^A e^{\ell g(h)}
                    \max\{1,e^{-2\pi y\ell}\},
 \qquad a\le v\le1/2,\quad y\in\mathbb R .
 \tag{21}
\]
For real \(0\le v\le a\), equations (16)--(18) give instead
\[
 |\widehat P_{\ell,N}(\xi,e^{2\pi iv})|
 \le C N^A
     e^{\ell\{c(\cosh h-1)+\log\cos(\pi v)\}} .
 \tag{22}
\]
All statements are uniform in \(h\) on the displayed compact range.

## 3. Low physical indices and the complete outgoing contours

The only outgoing rows not directly covered by (21) are the
original low physical group \(0\le k\le\lfloor aN\rfloor\).
Let \(F(v)=\Re Q(v;1/2,z_*)\), with the original phase
\[
 Q(t;y,z)=g_{\rm fac}(y+t)+g_{\rm fac}(z+t)
       -2g_{\rm fac}(t)-g_{\rm fac}(y)-g_{\rm fac}(z)+2\pi iyt ,
 \tag{23}
\]
where \(g_{\rm fac}'(w)=\Log(1-e^{-2\pi iw})\) on its original
strip lift. This notation distinguishes it from the scalar
function \(g(h)\) in (5).
The sourcewise calibration and real-row estimate in the weighted
outgoing theorem give \(F(a)<E_*\) and, for \(0<v\le a\),
\[
 F'(v)=\log
 \frac{2\cos(\pi v)|1-Z_*e^{-2\pi iv}|}
                         {4\sin^2(\pi v)}
 >\log2>\frac23 .
 \tag{24}
\]
The written witnesses in the fixed-ellipse proof are uniform:
\(2\cos\pi v\ge\sqrt3\), \(4\sin^2\pi v<1\),
\(\cos(2\pi(\Re z_*+v))<-3/10\), and
\(|1-Z_*e^{-2\pi iv}|^2>53/25>49/25\).

For each retained product degree,
\[
 \frac{d}{dv}\left[
  \frac{\ell}{N}\{c(\cosh h-1)+\log\cos(\pi v)\}\right]
 =-\frac{\ell\pi}{N}\tan(\pi v)>-\frac{22}{35}.
 \tag{25}
\]
Here \(\ell/N<1/3\), \(\tan(\pi v)<1/\sqrt3<3/5\),
and \(\pi<22/7\). Since \(2/3>22/35\), (24)--(25)
show that the combined real-row upper rate increases to the
original cut:
\[
 F(v)+\frac{\ell}{N}
       \{c(\cosh h-1)+\log\cos(\pi v)\}
 \le F(a)+\frac{\ell}{N}g(h)
 <E_*+\frac{\ell}{N}g(h).
 \tag{26}
\]
Continuity includes \(v=0\); no derivative is used at its
singular endpoint. The exact row \(k=0\) is retained.
The replacement \(M/N\) by \(1/2\) in this rate comparison
costs only the original zero-safe \(O(\log N)\).

For the remaining finite rows use the same canonical interpolant
and exact split-cotangent identity as the weighted outgoing proof.
The cuts are
\[
 a_N=(\lfloor3N/20\rfloor+1/2)/N,\qquad
 b_N=(U+1/2)/N,\qquad M/N+b_N=1-\frac1{2N}.
 \tag{27}
\]
Thus the exact incoming numerator remains prewall at either
parity. Multiply its original canonical row by the entire product
\(\widehat P_{\ell,N}(\xi,e^{2\pi it})\). No pole, branch, or
normalization changes. Retain the \(+N\) real middle integral,
both horizontal cotangent remainders at heights \(-1/5,8\),
the upper and lower parts of both vertical sides, and both
unweighted joins to \(h_+=\max(h_t,0)\).

After factoring out the common number \(e^{\ell g(h)}\),
(21) gives precisely the old outgoing-height allowance, or a
smaller one: on lower heights its cost is \(2\pi\ell(-y)\),
with \(\ell<N/3\); on nonnegative heights its cost is zero.
Consequently the original argument bounds
\[
 -39\pi/50\le\Im Q_t\le11\pi/10
 \tag{28}
\]
leave the same lower-side decrease \(7\pi/30\), lower-horizontal
reserve \(37\pi/1500\), and upper-side decrease \(61\pi/50\).
The upper horizontal remains strictly below the main line.
The two full unweighted joins are bounded by their original
main or real-cut endpoints using the same private vertical
convexity. Each of these endpoints was calibrated profile by
profile at rate \(E_*\), before the finite summation.

The \(O(N^{-1})\) cut shifts in (27) and the possible half-index
numerator zero require only \(O(\log N)\) errors in (18),(21).
At the wall use the continuous two-branch factorial upper
envelope, without dividing by a period factor or asserting a
relative symbol there. The outgoing shifted real argument
remains below \(39/100+1/2<1\), as in the original source.
All constants are uniform in the spectral ellipse height on
\([0,H_{\max}]\). The polynomial cost includes the original
\(+N\), both cotangent prefactors, and every finite row.

Equation (26) pays the remaining low physical group with the
same common product factor. No rows above \(U\) are omitted:
they vanish exactly at the physical incoming node \(Y_N\).
This proves (6) for \(B_{\ell,N}^{\rm all}\), with any prescribed
positive finite allowance \(\tau\).

## 4. The original small-\(k\) subtraction

The positive finite bound in
[small outgoing indices, equations (9)--(14)](research_mixed_next_three_small_outgoing_indices.md)
is
\[
 \sum_{k=0}^{K}
 \left|\frac{Y_N^{-k}p_k(Y_N)p_k(Z_*)}{P_k^2}\right|
       \le N e^{N/200}.
 \tag{29}
\]
By (22), its product insertion costs at most
\(C N^A e^{\ell c(\cosh h-1)}\).
The cost relative to the target product factor \(e^{\ell g(h)}\)
is therefore independent of \(h\):
\[
 \frac1{200}+\frac{\ell}{N}\lambda
 <\frac1{200}+\frac1{12}
 =\frac{53}{600}
 <\frac{1459}{3000}<E_* .
 \tag{30}
\]
For the inequality \(\lambda<1/4\), use
\(\cos(3\pi/20)>\sqrt3/2>4/5>e^{-1/4}\);
the last comparison follows from \(e^{1/4}>1+1/4\).
Thus (29) may be subtracted absolutely at every allowed
ellipse height, retaining the factor \(e^{\ell g(h)}\).
This proves the other half of (6). Summing at most \(N\)
products gives (7).

This subtraction is made from the full coherent outgoing
observation. It does not infer a partial-sum bound from a
bound on the coherent sum. Both the complete polynomial and
its original \(k>K\) version are controlled separately.

## 5. Coefficient extraction and exact height optimization

Apply the Laurent coefficient formula to
\(B_{\ell,N}(\zeta+\zeta^{-1})\) on \(|\zeta|=e^h\).
Its Chebyshev coefficient of degree \(b\) vanishes for \(b>\ell\),
and otherwise is bounded by
\[
 2C_{\tau,H_{\max}}N^{A_{\tau,H_{\max}}}
       e^{N(E_*+\tau)+\ell g(h)-hb}.
 \tag{31}
\]
For \(b=0\) omit the factor two if desired. Summing only
\(\ell\ge b\) proves (9), with the finite number of degrees
absorbed into the polynomial prefactor. This argument works
also at \(h=0\) by the usual cosine coefficient formula.

The elementary bounds
\[
 \frac{35}{44}<c<1,\qquad 0<\lambda<\frac14,\qquad
 0<\rho_0<\frac34
 \tag{32}
\]
are sufficient to optimize uniformly. For the first bounds use
\(\sqrt3>5/3,\ \pi<22/7\) and
\(\sqrt3<7/4,\ \pi>25/8\); for the last,
\(\rho_0^2=2c\lambda+\lambda^2<9/16\).
In particular \(h_0<\operatorname{arsinh}(1/c)<\log3\):
indeed \(1/c<44/35<4/3=\sinh(\log3)\).

For \(0\le h\le h_0\), \(g(h)\le0\), so the exponent
depending on \(h,\ell\) in (9) is
\[
 b(g(h)-h).
 \tag{33}
\]
Its derivative is \(b(c\sinh h-1)\le b(\rho_0-1)<0\)
when \(b>0\). Its minimum is therefore at \(h=h_0\).
For \(h\ge h_0\) the exponent is instead
\[
 d\,g(h)-bh,
 \tag{34}
\]
whose derivative is \(d c\sinh h-b\).
Writing \(\rho=b/d\), its minimum on this interval is at
\(h_0\) if \(\rho\le\rho_0\), and otherwise at
\[
 h_\rho=\operatorname{arsinh}(\rho/c).
 \tag{35}
\]
All these heights are less than \(\log3\), by (32). Hence
Theorem 1 with the single compact range \(H_{\max}=\log3\)
justifies choosing a height depending on \(b/d\) and \(N\);
no nonuniform constants are optimized. Substitution in
(33)--(35) gives exactly (11)--(12).
For \(b=0\), \(h=h_0\) gives the same conclusion directly.

The two branches of \(I\) agree at \(\rho_0\), as do their
derivatives. On the upper branch
\[
 I'(\rho)=\operatorname{arsinh}(\rho/c),\qquad
 I''(\rho)=\frac1{\sqrt{c^2+\rho^2}}>0 .
 \tag{36}
\]
It follows that \(I(\rho)>h_0\rho\) for \(\rho>\rho_0\).

To compare the new weight with the previously adopted one,
the fixed-ellipse proof gives the exact written witnesses
\[
 c(\cosh(1/2)-1)\le\frac{5103}{47600},\qquad
 \lambda>\frac{225}{2048},\qquad
 \frac{225}{2048}-\frac{5103}{47600}>\frac1{400}.
 \tag{37}
\]
Thus \(g(1/2)<-1/400\) and \(h_0>1/2\).
Since \(g'(h)\le\rho_0<3/4\) on \([1/2,h_0]\),
\[
 \frac1{400}<g(h_0)-g(1/2)
       <\frac34(h_0-1/2).
 \tag{38}
\]
This proves (13). No approximate value of an optimizer,
coefficient, or reference action is used.

## 6. Exact use in the remaining observation

Keep the original functional and its modes from
[the outer observation theorem](research_mixed_next_three_outer_casimir_observation.md):
\[
 \mathcal L_N(P)=
 \phi_N^{(x)}
  [\mathcal R_N(x)^3e_M(x)\mathcal K_{3,N}(-2,x)P(x)],
 \qquad
 \mathcal L_{N,b}=\mathcal L_N(T_b(\cdot/2)).
 \tag{39}
\]
Linearity and (12) now give
\[
 |\mathcal L_N(H_N)|
 \le C_\tau N^{A_\tau}e^{N(E_*+\tau)}
       \sum_{b=0}^{d}e^{-d I(b/d)}|\mathcal L_{N,b}|.
 \tag{40}
\]
For example, it would suffice to prove
\[
 \max_{0\le b\le d}
       e^{-d I(b/d)}|\mathcal L_{N,b}|
       \le C N^B e^{N B_f},
 \qquad B_f=77/50+\pi/50.
 \tag{41}
\]
The original reserve between \(E_*+B_f\) and \(\Lambda\)
is unchanged. Estimate (41) is not proved here, nor is a
lower bound for the coherent trace asserted.

The original exact reduction still contains its scalar
\((-q)^M/(\kappa^2N)\), both Fourier coefficients, and all
previously accounted filter and boundary corrections. This
note changes only the justified bound on the actual outgoing
coefficients. It leaves the original full inner Hermite trace
and any eligible exact outer low-edge reduction intact.
No new outside-variable jets, full transfer asymptotic,
noncancellation conclusion, or arbitrary-short-cluster
statement follows from (12) alone.
