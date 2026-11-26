# A fixed positive-end spectral interval for the original signed source

This note proves a uniform exponential bound on a fixed interval adjacent to \(+2\). Its rate tends to zero with the interval width. The argument first combines the original one-step and two-step continuant paths, then estimates their exact Green expansion. It never substitutes the absolute local path expansion for the actual face numerator.

For a fixed matched-sphere source, the bound applies to the shared full coefficient, its CROSS projection, and their unsplit difference. It also bounds the part of the original full-Hermite filling sum in which every spectral node belongs to that interval. Thus it controls an actual part of the remaining source problem. It does not control mixed spectral regions or the whole spectral cube.

## 1. Finite statement and the original normalization

Put \(N\ge3\), \(d=N-1\), \(\theta=\pi/N\), and
\[
 c_j=2\cos((2j+1)\theta),\qquad s_j=2\sin(j\theta),\qquad
 \chi_N(t)=2T_N(t/2)+2.
 \tag{1}
\]
On the ordered monomials \(1,z,\ldots,z^d\), the actual face operator is
\[
 C(x,y)z^j=c_jz^j-s_j^2(x+y)z^{j-1}
                     -s_js_{j-1}xy z^{j-2}.
 \tag{2}
\]
Use its complete polynomial numerator
\[
 V_N(\sigma;C)=\chi_N(\sigma)(\sigma I-C)^{-1}.
 \tag{3}
\]
This denotes polynomial division, including at repeated roots. It retains the original normal data. The original four-face homogeneous polynomial has input and output middle exponents \(d-j,i\), and its outer exponents sum to \(j-i\). Thus its coefficient is exactly
\[
 [x^p y^{j-i-p}]\,[V_N(\sigma;C(x,y))]_{i,j},
 \qquad 0\le i\le j\le d.
 \tag{4}
\]
No level factor is added to (4).

For \(0<\delta\le1\), define
\[
 I_\delta=[2-\delta,2],\qquad
 C_\delta=1+\delta^{-1/2},\qquad
 \omega(\delta)=\sqrt\delta\left(2+
                           \log\left(1+\frac2{\sqrt\delta}\right)\right).
 \tag{5}
\]
If \(N\ge\pi/\sqrt\delta\), then every coefficient in (4) obeys
\[
 \boxed{
 \sup_{\sigma\in I_\delta}
 \left|[x^p y^{j-i-p}]
                  [V_N(\sigma;C(x,y))]_{i,j}\right|
       \le C_\delta N^3 e^{N\omega(\delta)}.
 }
 \tag{6}
\]
The interval is independent of the level, and \(\omega(\delta)\to0\) as \(\delta\downarrow0\). The assertion includes both level parities and every interval of original row indices. It holds at spectral nodes without dividing by their vanishing factors.

## 2. The signed recurrence and its exact free Green expansion

Set \(x=S,y=1\). The interval numerator is
\[
 \begin{aligned}
 P_{i,i}&=1,\qquad P_{i,i+1}=-s_{i+1}^2(1+S),\\
 P_{i,j}&=-s_j^2(1+S)P_{i,j-1}
       -s_js_{j-1}(\sigma-c_{j-1})S P_{i,j-2},\\
 [V_N(\sigma;C(S,1))]_{i,j}
       &=P_{i,j}(S)\prod_{r<i\ \mathrm{or}\ r>j}(\sigma-c_r).
 \end{aligned}
 \tag{7}
\]
The two negative arrows in (2) and the unused skipped-row factor give the recurrence directly. Normalize its monomer factor:
\[
 P_{i,i+k}=(-1)^k\left(\prod_{r=i+1}^{i+k}s_r^2\right)h_k(S).
 \tag{8}
\]
The elementary identity \(c_0-c_{j-1}=s_js_{j-1}\) gives
\[
 h_0=1,\quad h_1=1+S,\quad
 h_k=(1+S)h_{k-1}-S h_{k-2}+a_{i+k}S h_{k-2},
 \qquad a_j=\frac{c_0-\sigma}{s_js_{j-1}}.
 \tag{9}
\]
Write \(F_k(S)=1+S+\cdots+S^k\). Solving the free recurrence with a forcing term gives the exact polynomial identity
\[
 h_k(S)=F_k(S)+\sum_{r=2}^k
           a_{i+r}S F_{k-r}(S)h_{r-2}(S).
 \tag{10}
\]
For example, applying \(h_k-(1+S)h_{k-1}+Sh_{k-2}\) to the right side leaves only its \(r=k\) term. The initial values also agree. This proves (10) for every interval and spectral parameter.

Every coefficient of \(F_k\) is positive. Consequently, if \(a_j\ge0\), every coefficient of \(h_k\) is nonnegative, and in fact positive in every degree \(0,\ldots,k\). More generally the coefficientwise absolute value of \(h_k\) is bounded by the solution of (10) with each \(a_j\) replaced by any nonnegative upper bound on \(|a_j|\). This follows by induction in (10). The cancellation in the free term \((1+S)h-Sh\) has already been performed before this comparison.

For \(\sigma\in I_\delta\), our level condition gives
\[
 0<2-c_0=4\sin^2(\theta/2)\le\pi^2/N^2\le\delta,
 \qquad |c_0-\sigma|\le\delta.
 \tag{11}
\]
It therefore suffices to use the positive comparison coefficients
\[
                         A_j=\frac\delta{s_js_{j-1}}
                              \quad(2\le j\le d).
 \tag{12}
\]
Let \(Y_k\) be the corresponding solution at \(S=1\). Equation (10) implies both
\[
 |[S^p]h_k(S)|\le Y_k,
 \qquad \sup_{|S|=1}|h_k(S)|\le Y_k.
 \tag{13}
\]
Here the second inequality follows by the sum of the nonnegative comparison coefficients, not by discarding signs in (7).

## 3. A varying positive norm for the comparison recurrence

The recurrence for \(Y_k\), with \(Z_k=Y_k-Y_{k-1}\), is
\[
 Y_0=1,\quad Y_1=2,\quad Z_1=1,
 \qquad Z_k=Z_{k-1}+A_{i+k}Y_{k-2}.
 \tag{14}
\]
In particular \(Y_k,Z_k>0\), and \(Y_{k-2}\le Y_{k-1}\). Therefore
\[
 \binom{Y_k}{Z_k}
 \le
 \begin{pmatrix}1+A_{i+k}&1\\ A_{i+k}&1\end{pmatrix}
              \binom{Y_{k-1}}{Z_{k-1}}
 \tag{15}
\]
componentwise. For \(A>0\), define the positive linear norm on this quadrant by
\[
 \mathcal L_A(Y,Z)=Y+A^{-1/2}Z,
 \qquad \lambda(A)=1+\sqrt A+A.
 \tag{16}
\]
A direct multiplication proves
\[
 \mathcal L_A\left(
       \begin{pmatrix}1+A&1\\A&1\end{pmatrix}\binom YZ\right)
    \le\lambda(A)\mathcal L_A(Y,Z).
 \tag{17}
\]
Indeed the \(Y\) coefficient is exactly \(1+A+\sqrt A\), while the \(Z\) coefficient \(1+A^{-1/2}\) is at most \(\lambda(A)A^{-1/2}\).

The sequence \(A_j\) decreases and then increases, since
\[
 \sin(j\theta)\sin((j-1)\theta)
       =\frac{\cos\theta-\cos((2j-1)\theta)}2.
 \tag{18}
\]
On an increasing stretch of \(A\), the norm in (16) decreases at a fixed positive vector. On a decreasing stretch, changing \(A\) to \(A'\le A\) costs at most \(\sqrt{A/A'}\). These factors telescope. The elementary sine chord bound gives
\[
 \frac\delta4\le A_j\le\frac{\delta N^2}{16},
 \qquad
 \left(\frac{\max A_j}{\min A_j}\right)^{1/2}\le\frac N2.
 \tag{19}
\]
For the upper bound put \(k_j=\min(j-1,N-j)\ge1\). Both sines in (18) are at least \(2k_j/N\). The lower bound follows from \(s_js_{j-1}\le4\).

The initial norm is at most \(2+2/\sqrt\delta\). Combining (15)–(19), for every interval of length at least two,
\[
 Y_k\le N(1+\delta^{-1/2})
                \prod_{j=2}^{d}(1+\sqrt{A_j}+A_j).
 \tag{20}
\]
The product over all rows only enlarges the interval product. Length zero or one satisfies the resulting bound directly.

Because \(1+\sqrt A+A\le(1+\sqrt A)^2\), and each positive value of \(k_j\) occurs at most twice,
\[
 \begin{aligned}
 \sum_{j=2}^{d}\log(1+\sqrt{A_j}+A_j)
 &\le4\sum_{k=1}^{\lfloor N/2\rfloor}
                  \log\left(1+\frac{N\sqrt\delta}{4k}\right)\\
 &\le N\left[2\log(1+\sqrt\delta/2)
                +\sqrt\delta\log(1+2/\sqrt\delta)\right]\\
 &\le N\sqrt\delta\left[1+\log(1+2/\sqrt\delta)\right].
 \end{aligned}
 \tag{21}
\]
For the middle inequality integrate the decreasing function \(\log(1+A/x)\) from (0) to \(N/2\), with \(A=N\sqrt\delta/4\). Its integral is
\[
 B\log(1+A/B)+A\log(1+B/A),\qquad B=N/2.
 \tag{22}
\]
There is no level-dependent logarithmic loss in (21).

## 4. The unused factors and the coefficient bound

Put \(\gamma_r=2-c_r\). The positive endpoint monomer weight is
\[
 w_{i,j}^{+}=
       \left(\prod_{r=i+1}^{j}s_r^2\right)
           \prod_{r<i\ \mathrm{or}\ r>j}\gamma_r\le N^2.
 \tag{23}
\]
For completeness, set
\[
 U_j=\frac4{\gamma_0}\prod_{r=1}^j\frac{s_r^2}{\gamma_r},
 \qquad V_i=\frac{\gamma_i U_i}{4}.
 \tag{24}
\]
The full shifted sine product is \(\prod_r\gamma_r=4\), so \(w_{i,j}^{+}=U_j/V_i\). The adjacent ratios show that \(U_j\) decreases and then increases, with endpoints \(U_0=\csc^2(\theta/2)\le N^2\), \(U_d=N^2\). The sequence \(V_i=\prod_{r=1}^i\sin^2(r\theta)/\sin^2((r-1/2)\theta)\) increases and then decreases, with endpoints \(V_0=1\), \(V_d=N^2\sin^2(\theta/2)\ge1\). Hence \(U_j\le N^2\), \(V_i\ge1\), proving (23).

For our fixed interval, \(|\sigma-c_r|\le\gamma_r+\delta\). Thus the actual unused-factor weight is at most
\[
 N^2\prod_{r=0}^{d}\left(1+\frac\delta{\gamma_r}\right)
 =N^2\frac{\chi_N(2+\delta)}4
 \le N^2 e^{N\sqrt\delta}.
 \tag{25}
\]
Indeed, if \(\kappa=\operatorname{arcosh}(1+\delta/2)\), the ratio is \(\cosh^2(N\kappa/2)\le e^{N\kappa}\), and \(\kappa\le\sqrt\delta\). Equations (13), (20), (21), and (25) prove (6). This argument uses the unused product without dividing by any physical \(\sigma-c_r\), so spectral collisions introduce no exception.

## 5. The actual shared coefficient and its finite filling contribution

Let \(r\) be the number of matching boxes of the fixed original diagram. Take the shared coefficient with its original protected faces, ordinary targets, unrestricted mark, cups and caps, as in the general Morse source theorem. Write \(S_N^{\mathrm{full}}\), \(S_N^{\mathrm C}\), and \(D_N=S_N^{\mathrm{full}}-S_N^{\mathrm C}\) for its full polynomial, CROSS polynomial, and unsplit difference.

There are at most \(N^3\) monomials in a four-face homogeneous polynomial of degree \(d\). The original CROSS projection selects the original input/output intervals; it preserves the signed continuant within each selected entry. Consequently (6), followed by the original shared coefficient extraction, gives
\[
 \begin{aligned}
 \sup_{I_\delta^r}|S_N^{\mathrm{full}}|,
 \ \sup_{I_\delta^r}|S_N^{\mathrm C}|
        &\le C_\delta^rN^{6r}e^{Nr\omega(\delta)},\\
 \sup_{I_\delta^r}|D_N|
        &\le2C_\delta^rN^{6r}e^{Nr\omega(\delta)}.
 \end{aligned}
 \tag{26}
\]
All ordinary demands, including the single common south-pole demand of the bipyramid, are imposed before this estimate. There is no optimization over separate face radii and no independent boundary target replacement.

This has a precise consequence inside the actual finite spectral sum. Let \(\mathcal L_{N,I}^{n}\) be the original full-Hermite functional restricted to the distinct double roots \(c_a\in I=I_\delta\):
\[
 \mathcal L_{N,I}^{n}H
 =\frac1{N^2}\sum_{c_a\in I}
     \left[(4-c_a^2)(f_nH)'(c_a)-c_af_n(c_a)H(c_a)\right].
 \tag{27}
\]
Here \(f_n\) is the actual full crossing polynomial, with its original Cartan factor and signed normal derivative. Its values have modulus one, and
\[
 (4-c_a^2)|f_n'(c_a)|\le |n|N,
 \qquad 4-c_a^2\le4\delta\quad(c_a\in I).
 \tag{28}
\]
These follow from \(f_n(2\cos\phi)=q^{nd^2/4}\exp(inN(\phi-\pi)^2/(4\pi))\). The odd simple root \(-2\) is outside \(I\); it has not been removed from the complementary part of the full functional.

The interval Markov inequality is
\[
 \|H'\|_I\le\frac{2d^2}{\delta}\|H\|_I.
 \tag{29}
\]
It also holds for complex coefficients: at a point maximizing the derivative, multiply by a unit complex number and take the real part before applying the real inequality. There are at most \(N/2\) distinct double roots. Hence
\[
 |\mathcal L_{N,I}^{n}H|
 \le\left(\frac{4d^2}{N}+\frac{|n|}{2}+\frac1N\right)\|H\|_I.
 \tag{30}
\]
Apply this coordinate by coordinate to the original shared polynomial. For the unsplit difference one can also retain its exact vanishing on the product node grid. Put
\[
 a_N=\frac{4d^2}{N},\qquad b_{e,N}=\frac{|n_e|}{2}+\frac1N.
 \tag{30a}
\]
In (27), the term multiplying \(H'(c_a)\) defines a derivative operator of norm at most \(a_N\), while the two terms multiplying \(H(c_a)\) define a value operator of norm at most \(b_{e,N}\). The tensor product consisting entirely of value operators annihilates \(D_N\), since full and CROSS agree on the whole product node grid. Expand the tensor product of these exact operators before estimating. Every remaining term contains at least one derivative operator. Thus, for fixed signed powers \(\boldsymbol n\),
\[
 \left|\left(\bigotimes_{e=1}^r\mathcal L_{N,I}^{n_e}\right)D_N\right|
 \le 2C_\delta^rN^{6r}
       \left\{\prod_e(a_N+b_{e,N})-\prod_e b_{e,N}\right\}
                    e^{Nr\omega(\delta)}.
 \tag{31}
\]
The derivative operators are still evaluated at nodes inside \(I\). The bound on each derivative comes from (29) on that same interval; no derivative at an exterior point, and no interpolation across an omitted node, is used.
This is a genuine part of the original full-minus-CROSS contraction: every selected normal term is retained. It is not a new invariant. No further quantum dimension or measure is multiplied into (31); the general Morse identity has already canceled those factors. The external zero-framing/component phase has modulus one, and the separately specified modified one-cut normalization is polynomial in the level.

Let \(\Phi=\operatorname{Vol}(Y)/(2\pi)>0\) be the original drilled action. Choose a fixed \(\delta\) such that \(r\omega(\delta)<\Phi/2\). This is always possible. For an explicit choice, put \(\delta=2^{-2K}\) and take an integer \(K\ge1\) with
\[
                   r(K+4)2^{-K}<\Phi/2.
 \tag{32}
\]
The inequality \(\omega(2^{-2K})\le(K+4)2^{-K}\) follows directly from (5). The established all-CROSS filling theorem has action tending to \(\Phi\) as the fixed signed fillings become independently long. Thus (31) is strictly below that nonzero geometric contribution for all sufficiently long fixed fillings. This suppresses the joint positive-end node region. It does not suppress regions in which only some coordinates belong to \(I\), nor any remaining portion of the original sum.

## 6. Why a polynomial extension to a fixed interval is false locally

The exponential allowance in (6) is necessary for the individual original coefficients. Fix \(0<\delta\le1\), set \(\sigma=2-\delta\), and take \(N\) sufficiently large that \(c_0-\sigma\ge\delta/2\). All coefficients \(a_j\) in (9) are then positive and at least \(a=\delta/8\). By the positive Green expansion, the full interval satisfies
\[
 h_d(1)\ge
 \frac{(1+\sqrt a)^{d+1}-(1-\sqrt a)^{d+1}}{2\sqrt a}
 \ge(1+\sqrt a)^d.
 \tag{33}
\]
The constant-coefficient expression has initial values \(1,2\) and solves (9) at \(S=1\). Coefficientwise monotonicity in the nonnegative \(a_j\) proves the first inequality. The second uses \(0<a<1\).

There are no unused rows in the interval \(0,\ldots,d\), and \(\prod_{j=1}^d s_j^2=N^2\). Since its \(N\) coefficients are nonnegative after the sign \((-1)^d\), at least one original coefficient has magnitude
\[
 \max_{0\le p\le d}
 \left|[x^py^{d-p}]
             [V_N(2-\delta;C(x,y))]_{0,d}\right|
       \ge N(1+\sqrt{\delta/8})^{N-1}.
 \tag{34}
\]
Thus the polynomial endpoint bound cannot hold uniformly on any fixed interval reaching below (2). This is an obstruction only to that stronger local assertion. The actual shared contraction can cancel such coefficients, so (34) is not a lower bound on \(D_N\) or a counterexample to its desired strict global gap.

## 7. A sign factor available for actual sewing

The Green expansion also gives an exact sign description on a real interval between nodes. Assume \(-2<\sigma<c_0\) and \(\chi_N(\sigma)>0\). Put
\[
 b_j=\operatorname{sgn}(\sigma-c_j),\qquad
 D_i=(-1)^i\prod_{r<i}b_r.
 \tag{35}
\]
All coefficients of the normalized \(h_{i,j}\) are positive. Since \(c_{d-r}=c_r\) and \(\prod b_r=1\), the sign of every coefficient in the original entry is
\[
 \operatorname{sgn}
 \left([x^py^{j-i-p}][V_N(\sigma;C(x,y))]_{i,j}\right)
       =(-1)^dD_iD_{d-j}.
 \tag{36}
\]
To verify it, (7)–(8) give \((-1)^{j-i}\prod_{r<i\ \mathrm{or}\ r>j}b_r\). Reflection identifies \(\prod_{r>j}b_r\) with \(\prod_{r<d-j}b_r\), which is exactly (36). The two indices \(i,d-j\) are the actual middle exponents. The sign is independent of the split between the two outer faces.

At even levels and \(\sigma=-2\), every \(b_j=-1\), so \(D_i=1\) for all indices and every coefficient has sign \((-1)^d\). The corresponding complementary source at a common \(-2\) tuple is therefore an unsigned sum after its one global sign. For other spectra the middle-exponent signs remain in the shared coefficient extraction; one may not remove them independently at adjacent boxes. Formula (36) supplies that exact sign data, but proves no cancellation around the cyclic grade paths.

The remaining target is the strict estimate for \(D_N\) on the whole cube \([-2,2]^r\), with the original shared demands. Equations (26) and (31) settle one fixed corner and its actual normal contribution. Equations (34) and (36) explain why extending the endpoint argument by a uniform polynomial local norm, or by pretending that every local coefficient is positive, would be invalid.
