# Exact Jackson reconstruction of the original crossing boundary jets

Private written proof, 17 November 2026. This concerns the full original
fixed-root crossing polynomial, including its Hermite data and scalar.
It gives all protected-face occupation coefficients, without replacing
them by values of a classical kernel. No positivity, boundary Gaussian
coefficient, or genuine-q continuation is asserted.

## 1. The original coefficient and two finite translations

Use [H], with \(N\ge3\), \(d=N-1\), \(q=e^{\pi i/N}\),
\(Q=q^2\), \(S_j=\prod_{a=1}^j2\sin(\pi a/N)\), and \(S_0=1\).
For \(\sigma\in\{1,-1\}\), write
\(H_\sigma=H_{R^\sigma}(x,b,c,y)\) and retain the original
\(\lambda_0^\sigma=q^{\sigma d^2/2}\), on its prescribed lift.
Its exact coefficient is
\[
 [b^i x^k y^l c^t]H_\sigma
 =\lambda_0^\sigma(-1)^{k+l+1}
 q^{\sigma(kl-(i+1)(t+1))}
 \frac{N}{S_iS_kS_lS_t},\qquad i+k+l+t=d. \tag{1}
\]
This is the actual full Casimir polynomial, not value interpolation.

Put \(\tau=Q^\sigma\), and define
\[
 [j]_\tau=\frac{1-\tau^j}{1-\tau},\quad
 [j]_\tau!=\prod_{a=1}^j[a]_\tau,\quad
 D_{\tau,z}f=\frac{f(\tau z)-f(z)}{(\tau-1)z}. \tag{2}
\]
The last expression is a polynomial operator, including at \(z=0\).
Every factorial in (2) with \(j<N\) is a unit. Define
\[
 B_m^\tau(X,Y)=\sum_{r=0}^m{m\brack r}_\tau X^rY^{m-r},
 \qquad {m\brack r}_\tau=\frac{[m]_\tau!}{[r]_\tau![m-r]_\tau!}.
\]
For \(m<N\), direct sine conversion gives
\[
 {m\brack r}_{Q^\sigma}
 =q^{\sigma r(m-r)}\frac{S_m}{S_rS_{m-r}}. \tag{3}
\]

**Exact reconstruction.** The following are polynomial identities:
\[
\begin{split}
 H_\sigma(x,b,c,y)
 &=\sum_{k=0}^d\frac{x^k}{[k]_\tau!}
       D_{\tau,y}^{\,k}H_\sigma(0,b,c,y),\\
 &=\sum_{i=0}^d\frac{b^i}{[i]_{\tau^{-1}}!}
       D_{\tau^{-1},c}^{\,i}H_\sigma(x,0,c,y),\\
 &=\lambda_0^\sigma\sum_{m=0}^d(-q^\sigma)^m
        B_m^\tau(x,y)B_{d-m}^{\tau^{-1}}(b,c). \tag{4}
\end{split}
\]
The symmetric formulas exchange \(x,y\), or \(b,c\).
They also give the global polynomial equations
\[
 D_{\tau,x}H_\sigma=D_{\tau,y}H_\sigma,\qquad
 D_{\tau^{-1},b}H_\sigma=D_{\tau^{-1},c}H_\sigma. \tag{4a}
\]

To prove the first line, compare the coefficient in (1) with the
coefficient having \(k=0\) and outer degree \(l+k\). Their ratio is
\(q^{\sigma kl}S_{k+l}/(S_kS_l)={k+l\brack k}_\tau\).
This is exactly the coefficient produced by
\(D_{\tau,y}^{\,k}/[k]_\tau!\). For the second line the analogous
ratio is \(q^{-\sigma it}S_{i+t}/(S_iS_t)\).
The two translations commute because their operators use different
variables. Their common initial polynomial is
\[
 H_\sigma(0,0,c,y)
       =\lambda_0^\sigma\sum_{m=0}^d(-q^\sigma)^m c^{d-m}y^m. \tag{5}
\]
Applying both translations proves the last line of (4). Equivalently,
use \(S_mS_{d-m}=N\) in (3); its phase agrees with (1) because
\(i+k+l+t=N-1\). This proves every constant and sign at both parities.
There is no division by \([N]_\tau=0\).

In particular every ordinary boundary derivative is known exactly:
\[
 \left.\partial_x^kH_\sigma\right|_{x=0}
       =\frac{k!}{[k]_\tau!}D_{\tau,y}^{\,k}H_\sigma(0,b,c,y). \tag{6}
\]
The corresponding middle formula uses \(\tau^{-1}\); mixed jets follow
from the commuting translations. These are finite face derivatives,
not derivatives of a root-only formula with respect to \(q\).

## 2. First occupation at one or two zero faces

At one zero the four rules are
\[
\begin{array}{c|c}
\text{zero face}&\text{first occupation}\\ \hline
x&\partial_xH_\sigma|_{x=0}=D_{\tau,y}(H_\sigma|_{x=0})\\
y&\partial_yH_\sigma|_{y=0}=D_{\tau,x}(H_\sigma|_{y=0})\\
b&\partial_bH_\sigma|_{b=0}=D_{\tau^{-1},c}(H_\sigma|_{b=0})\\
c&\partial_cH_\sigma|_{c=0}=D_{\tau^{-1},b}(H_\sigma|_{c=0}).
\end{array} \tag{7}
\]
Apply these before identifying repeated face variables.

For **adjacent** zeros take \(x=b=0\), with ordinary outer \(y\)
and ordinary middle \(c\), and write \(B=H_\sigma(0,0,c,y)\).
Then
\[
\begin{split}
 (c+q^{3\sigma}y)\,\partial_xH_\sigma|_{x=b=0}&=-q^\sigma B,\\
 (c+q^{3\sigma}y)\,\partial_bH_\sigma|_{x=b=0}&=-q^{2\sigma}B. \tag{8}
\end{split}
\]
These undivided polynomial identities hold everywhere. Thus on a
nonzero chart the two logarithmic occupation ratios are respectively
\(-q^\sigma/(c+q^{3\sigma}y)\) and
\(-q^{2\sigma}/(c+q^{3\sigma}y)\). In particular the second jet
is \(q^\sigma\) times the first. All four adjacent patterns follow
by the two separate pair symmetries.

For proof, (5) gives
\[
 B=\lambda_0^\sigma\frac{c^N-(-1)^{N+1}y^N}{c+q^\sigma y}. \tag{9}
\]
Its numerator is invariant under \(y\mapsto\tau y\) and
\(c\mapsto\tau^{-1}c\). Subtract the two rational expressions and
use (7); clearing denominators proves (8), also at their zeros.

For **opposite outer** zeros, put
\(O(b,c)=H_\sigma(0,b,c,0)=\lambda_0^\sigma B_d^{\tau^{-1}}(b,c)\).
Then
\[
 \partial_xH_\sigma|_{x=y=0}=\partial_yH_\sigma|_{x=y=0}
 =q^{-\sigma}D_{\tau^{-1},b}O
 =q^{-\sigma}D_{\tau^{-1},c}O
 =-\lambda_0^\sigma q^\sigma B_{d-1}^{\tau^{-1}}(b,c). \tag{10}
\]
For **opposite middle** zeros, put
\(I(x,y)=H_\sigma(x,0,0,y)
=\lambda_0^\sigma(-q^\sigma)^dB_d^\tau(x,y)\). Then
\[
 \partial_bH_\sigma|_{b=c=0}=\partial_cH_\sigma|_{b=c=0}
 =q^\sigma D_{\tau,x}I=q^\sigma D_{\tau,y}I
 =\lambda_0^\sigma(-q^\sigma)^{d-1}B_{d-1}^\tau(x,y). \tag{11}
\]
Indeed \(D_{\tau,X}B_d^\tau=D_{\tau,Y}B_d^\tau
=[d]_\tau B_{d-1}^\tau\), and \([d]_\tau=-\tau^{-1}\).
Alternatively (10)--(11) are the terms \(m=1,d-1\) of (4).
Further zero specializations follow from these polynomial identities.
Four zero arguments give the zero polynomial since \(d>0\).

There is a uniform local consequence at an adjacent corner. Write its
remaining variables as \(u=y,v=c\), put \(a=q^\sigma\), and set
\[
 A_j=v+a\tau^j u,\qquad C_0=v^N-(-au)^N,\qquad
 B=H_\sigma(0,0,v,u)=\lambda_0^\sigma C_0/A_0.
\]
For restored outer \(X\) and middle \(Z\), the full formula is
\[
 \frac{H_\sigma(X,Z,v,u)}{B}
 =\sum_{\substack{k,l\ge0\\k+l\le d}}
 \frac{(-a)^k(-1)^l\tau^{l(l+1)/2}
             {k+l\brack l}_\tau X^kZ^l}
      {\prod_{j=1}^{k+l}A_j}. \tag{11a}
\]
The empty denominator is one. This is first a rational identity on
the nonzero chart; the corresponding undivided polynomial identity
is (4). To prove it, both shifts preserve \(C_0\), and
\[
 \frac{D_{\tau,u}^k(C_0/A_0)}{[k]_\tau!}
       =\frac{(-a)^kC_0}{A_0\cdots A_k},\qquad
 D_{\tau^{-1},v}\frac{C_0}{A_0\cdots A_k}
       =-\tau[k+1]_\tau\frac{C_0}{A_0\cdots A_{k+1}}. \tag{11b}
\]
Iterate the second identity and use
\([l]_{\tau^{-1}}!=\tau^{-l(l-1)/2}[l]_\tau!\).
The last allowed denominator is the full product \(C_0\);
the next difference has factor \([N]_\tau=0\), so no endpoint is lost.

If \(\big||v|-|u|\big|\ge\delta>0\) and
\(|X|+|Z|\le r\delta\), \(0\le r<1\), then \(B\ne0\),
every \(|A_j|\ge\delta\), and
\[
 \left|\frac{H_\sigma(X,Z,v,u)}B-1\right|
       \le\sum_{m=1}^d r^m\le\frac r{1-r}. \tag{11c}
\]
Indeed \(|{m\brack l}_\tau|\le\binom ml\), since the Gaussian
binomial is a polynomial with nonnegative integer coefficients whose
value at one is \(\binom ml\); its elementary recurrence proves
this assertion. Thus \(r<1/2\) gives a uniform nonzero analytic ratio
with lower bound \((1-2r)/(1-r)\) and upper bound \(1/(1-r)\),
at every level. Buffered versions give uniform fixed derivatives by
Cauchy's formula. This is an adjacent-corner statement with an explicit
radial separation, not an assertion that an original ordinary saddle
satisfies that separation. No opposite-corner bound is inferred.

The same exact formula also resolves one equal-modulus corner. Set
\(v=-au\), where \(u\ne0\). Although \(C_0=A_0=0\), the polynomial
value and every denominator in (11a) are now
\[
 B=\lambda_0^\sigma N(-au)^d,\qquad
 A_j=au(\tau^j-1)\quad(1\le j<N).
\]
Consequently, locally uniformly for complex \((\xi,\eta,u)\) with
\(u\ne0\),
\[
 \frac{H_\sigma(\xi/N,\eta/N,-au,u)}
      {\lambda_0^\sigma N(-au)^d}
 =\exp\!\left(-\frac{\xi+\eta}{2\pi i\sigma u}\right)
       \bigl(1+O(N^{-1})\bigr). \tag{11d}
\]
The same statement holds after every fixed complex derivative on
buffered compact sets. In particular the normalized polynomial is
zero-free on each such compact for all sufficiently large \(N\).
This is a packet at the specified adjacent corner, not a claim for
all equal-modulus quartets or for an assembled saddle. In particular
\(v=-q^\sigma u\) is not the literal slice \(v=-u\) produced by
equal dephased ordinary coordinates with opposite checkerboard signs;
their order-\(N^{-1}\) displacement is on the scale of (11d).

Here is a direct uniform proof. Continue (11a) to \(v=-au\);
the displayed \(B\) is nonzero and \(A_1,\ldots,A_d\) remain units.
For \(m=k+l\), its summand is
\[
 \frac{(-1)^m a^{-l}\tau^{l(l+1)/2}{m\brack l}_\tau
              \xi^k\eta^l}
      {N^m u^m\prod_{j=1}^m(\tau^j-1)}. \tag{11e}
\]
At fixed \(m\), summing over \(l\) converges to
\([-(\xi+\eta)/(2\pi i\sigma u)]^m/m!\).
On a compact let \(|\xi|+|\eta|\le R\), \(|u|\ge u_*>0\).
For \(m\le N/2\), the absolute grouped term is at most
\[
 \frac{(R/(Nu_*))^m}{S_m}
 \le\frac{(R/(4u_*))^m}{m!},
 \qquad S_m\ge(4/N)^m m!.
\]
For \(m>N/2\), use \(S_m=N/S_{d-m}\ge N2^{-(d-m)}\);
the sum of these terms is bounded by
\(N^{-1}\sum_{m>N/2}^{d}(R/(Nu_*))^m2^{d-m}\), which is
superexponentially small. This proves uniform convergence.
For the stated error, restrict first to \(m\le N^{1/4}\).
The three normalized factors
\[
 a^{-l}\tau^{l(l+1)/2},\quad
 {m\brack l}_\tau/\binom ml,\quad
 \frac{N^m\prod_{j=1}^m(\tau^j-1)}
      {(2\pi i\sigma)^m m!}
\]
are \(1+O(m^2/N)\), uniformly in \(l\). For the middle factor
use its nonnegative coefficient polynomial of degree \(l(m-l)\);
for the last, multiply the elementary exponential expansions.
Summing the resulting factorial majorant gives \(O(N^{-1})\);
the remaining factorial tail is smaller. The exponential limit has
a positive modulus minimum on each compact, giving the relative
form (11d). Cauchy's formula proves its derivative version.

For the literal slice \(v=-u\), the corresponding result is different.
Set
\[
 \widetilde B=H_\sigma(0,0,-u,u)
     =\lambda_0^\sigma\frac{2(-1)^Nu^d}{q^\sigma-1},
 \qquad t=-\frac{\xi+\eta}{2\pi i\sigma u},
 \qquad
 \mathcal F(t)=\sum_{m=0}^{\infty}\frac{t^m}{(3/2)_m}.
\]
Here \((3/2)_m=\prod_{j=1}^m(j+1/2)\), with empty product one;
equivalently \(\mathcal F={}_1F_1(1;3/2;\,\cdot\,)\).
Then on every compact complex parameter set with \(u\ne0\),
\[
 \frac{H_\sigma(\xi/N,\eta/N,-u,u)}{\widetilde B}
        =\mathcal F(t)+O(N^{-1}). \tag{11f}
\]
The estimate holds after every fixed derivative on buffered compacts.
On compact sets with \(|t|\le1/4\), it is a relative
\(\mathcal F(t)(1+O(N^{-1}))\) estimate and gives a zero-free
normalized polynomial for all sufficiently large \(N\). There is
no assertion of zero-freeness on arbitrary complex parameter compacts.

For proof, (9) gives the displayed nonzero \(\widetilde B\), and
now \(A_j=u(q^\sigma\tau^j-1)\) for \(1\le j<N\). At fixed
total degree \(m\), (11a) therefore converges to
\(t^m/(3/2)_m\). A single factorial majorant works up to the
actual root endpoint. Indeed, for \(1\le j\le m\le N-1\),
\[
 \min(j+1/2,N-j-1/2)
 \ge\tfrac12\min(j,N-j)
 \ge\tfrac12\min(j,m+1-j).
\]
The product of the last minima is
\(\lfloor m/2\rfloor!\lceil m/2\rceil!\ge m!/2^m\).
Using \(\sin(\pi s)\ge2\min(s,1-s)\) on \([0,1]\), obtain
\[
 \prod_{j=1}^m|q^\sigma\tau^j-1|
 =\prod_{j=1}^m2\sin\!\frac{\pi(j+1/2)}N
 \ge\frac{m!}{N^m}. \tag{11g}
\]
Thus the absolute grouped term is at most
\((R/u_*)^m/m!\) on the preceding parameter compacts.
For \(m\le N^{1/4}\), the phase, Gaussian binomial, and
normalized denominator expansions have relative error
\(O(m^2/N)\), exactly as in (11e), now with \(j+1/2\).
Summing gives \(O(N^{-1})\), and the remaining factorial tail
is smaller. This proves (11f) and its derivative version.
Finally \((3/2)_m\ge m!\), so
\(|\mathcal F(t)-1|\le e^{|t|}-1\).
On \(|t|\le1/4\), its modulus is at least \(2-e^{1/4}>0\);
the asserted local relative estimate follows. Both (11d) and (11f)
concern the exact crossing polynomial with its full scalar, rather
than an assumed off-critical determinant or co-source adapter.

The ordinary contrast has a separate scale that must also be retained.
For complex \(s\), let
\[
 B(s)=H_\sigma(0,0,-ue^s,u)
   =\lambda_0^\sigma(-1)^Nu^d
        \frac{e^{Ns}+1}{a-e^s},\qquad a=q^\sigma. \tag{11h}
\]
All apparent singularities in this expression are removable when
interpreted as the polynomial (5). In a neighborhood of \(s=0\),
where \(B\ne0\), exact differentiation gives
\[
 \left.\partial_s^2\log B(s)\right|_{s=0}
 =\frac{N^2}{4}+\frac{a}{(a-1)^2}
 =\frac{N^2}{4}-\frac1{4\sin^2(\pi/(2N))}
 =N^2\left(\frac14-\frac1{\pi^2}\right)+O(1). \tag{11i}
\]
In particular this contrast cannot be treated as having only
order-\(N\) logarithmic curvature.

Its exact scaled profile and limit are
\[
 \frac{B(\delta/N)}{B(0)}
  =\frac{e^\delta+1}{2}\frac{a-1}{a-e^{\delta/N}}
  =\Phi_\sigma(\delta)\bigl(1+O(N^{-1})\bigr),\qquad
 \Phi_\sigma(\delta)=
   \frac{\pi i\sigma(e^\delta+1)}{2(\pi i\sigma-\delta)}. \tag{11j}
\]
The value at \(\delta=\pi i\sigma\) is removable. More precisely,
put \(c_\sigma=\pi i\sigma\) and \(E(z)=(e^z-1)/z\), \(E(0)=1\).
Then the exact analytic factorization is
\[
 \frac{B(\delta/N)}{B(0)}
   =\Phi_\sigma(\delta)
       \frac{E(-c_\sigma/N)}
            {E((\delta-c_\sigma)/N)}. \tag{11k}
\]
On every fixed complex compact, the last quotient is holomorphic
for large \(N\) and is \(1+O(N^{-1})\), with all fixed derivatives.
This also proves convergence through the removable point, without
dividing an estimate by its vanishing numerator.

For an explicit nonzero neighborhood, on \(|\delta|\le1/4\),
\[
 |\Phi_\sigma(\delta)-1|
 \le
 \frac{(e^{1/4}-1)/2+1/(4\pi)}{1-1/(4\pi)}
 <\frac12.
\]
Thus (11j) gives a uniform relative, zero-free local contrast packet.
Indeed the exact finite profile is already nonzero on this disk:
\(e^\delta+1\) has no zero there, and neither does its displayed
denominator. The constant \(\lambda_0^\sigma\) and the ordinary
power \(u^d\) have only canceled in the normalized ratio; they remain
in (11h). Equations (11h)--(11k) identify an actual \(N^{-1}\)
ordinary contrast layer. They do not assert a critical point, a
Gaussian approximation in the remaining faces, or compatibility
with an unproved global boundary contour.

## 3. Exact assembly, with every repeated incidence retained

For the original numerator \(\mathcal P_N=\prod_eH_{f_e}\), let
\(B_e\) be the literal specialization at the two protected faces.
For a protected face \(u\), let \(J_{e,u}\) be the sum of local first
derivatives over every slot of box \(e\) carrying \(u\), evaluated
afterwards at the protected zeros. The exact identity is
\[
 (\mathcal P_N)_u|_0
       =\sum_e J_{e,u}\prod_{f\ne e}B_f. \tag{12}
\]
It holds with repeated faces and with vanishing factors, without
division. If \(\mathcal P_N|_0\ne0\), division yields
\((\mathcal P_N)_u/\mathcal P_N=\sum_eJ_{e,u}/B_e\).
Equations (7)--(11) supply these local terms for signed crossings.
Higher occupations use ordinary product coefficient convolution and
(6), retaining every allocation of the total occupation.
Under a fixed unit change \(L_f=\gamma_fR_f\), each derivative with
respect to \(R_u\) multiplies the corresponding \(J_{e,u}\) by
\(\gamma_u\). Thus any original face signs or units remain in (12);
the formulas here use the literal \(H\)-variables throughout.

This sum is not generally one Jackson derivative of the product.
For a common variable and shift, the exact product rule is
\[
 D_{\tau,z}(fg)=(D_{\tau,z}f)g+f(\tau z)D_{\tau,z}g. \tag{13}
\]
The unshifted sum in (12) differs by
\((f(\tau z)-f(z))D_{\tau,z}g\), with its displayed order and sign
when subtracting the unshifted sum from (13). Different neighboring
signs or opposite variables give still different operators.
An ordinary logarithmic critical equation therefore does not remove
these finite shifts. Since the degrees grow with \(N\), their shifts
cannot be replaced by ordinary derivatives solely because \(Q\to1\).

The actual ordinary target nevertheless gives an exact adjoint rule.
For polynomials \(f,g\), whose coefficients may involve every other
face, put \(I_d=[z^d]\). Then
\[
 I_d[(D_{\tau,z}f)g]
       =-\tau^{-1}I_d[fD_{\tau^{-1},z}g]. \tag{13a}
\]
In each contributing pair of monomials their original degrees satisfy
\(a+b=d+1=N\), and
\([b]_{\tau^{-1}}=-\tau[a]_\tau\). This proves (13a), including
the zero endpoint factors. In particular \(I_dD_{\tau,z}(fg)=0\).
The right side of (13a) retains the entire spectator product.
Expanding it uses the shifted rule (13); it does not select a single
next box or eliminate the resulting cycle and boundary terms.

## 4. Signed powers and the arbitrary-coupon boundary

The definition of \(H_f\) in [H] directly gives, for two operators on
the same original pair,
\[
 H_{FG}(x,b,c,y)=[z^d]H_F(x,b,z,y)H_G(x,z,c,y). \tag{14}
\]
To check the normalization, expand both operators on input monomials.
The exponent \(d-j\) in the first kernel pairs with the output degree
\(j\) of the second; the remaining coefficient is their ordinary
matrix product. No additional \(N\) or mark occurs.

Thus any fixed integer crossing power uses (14) on its literal signed
layers, retaining \(\lambda_0^p\). Protected outer derivatives act on
all factors by the usual Leibniz rule; external middle derivatives act
on their incident end factors. Coefficient extraction commutes with
these operations. This gives exact boundary jets of arbitrary signed
powers without asserting that their fused kernel obeys the one-layer
Jackson rule. Opposite layers can cancel to the identity.

An arbitrary Casimir coupon still uses its entire \(H_f\), its exact
product rule (12), and convolution (14). It is not assigned (4):
already \(H_1=\sum_{j=0}^d b^jc^{d-j}\) has
\(\partial_bH_1|_{b=0}=c^{d-1}\), whereas
\(D_{\tau^{-1},c}c^d=-\tau c^{d-1}\), different for \(N\ge3\).
The finite formulas above retain the original full-normal source;
they neither make all its coefficients positive nor force a nonzero
assembled protected occupation or selected scalar.

## Direct source and coverage

[H] [Homogeneous original Casimir face source](actual_homogeneous_casimir_face_source.md),
SHA-256 `a7d89f310f2cb4193ab73ef49f715198b224d1c3756d84c4cb940d7fa850c2f2`.
Its entire proof supplies the original kernel, full Hermite scope,
coefficient (1), and literal marked assembly. The geometric series
(5) and its signed cap contraction already occur in
[the trace-one cap interface](research_trace_one_mark_and_cap_turn_interface.md),
Section 3. The additional calculation here is the finite two-pair
Jackson reconstruction and its complete protected-jet consequences.
No existing geometric or quantum-normal scope is enlarged.
