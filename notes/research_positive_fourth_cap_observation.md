# A nonzero observation of the fourth positive cap moment

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The positive cap moments have a better lower bound than the one obtained
from their second and third moments alone. The new bound comes from one
specified coefficient of the original vector \(H^2e_0\). At that
coefficient the summation variable has a real stationary point. Its
absolute amplitude has a unique global maximum there, so the local
complex Gaussian cannot be canceled by the remaining summands.

The result improves the exponential lower bound for every fixed capped
chain of length at least four. It does not determine the sharp fourth
moment, or identify these bounds with a knot-complement volume.

## 1. The original coefficient and its known input

Use the original crossing matrix \(M\), reversal \(J\), and cap \(e_0\)
from [the positive-cycle theorem](research_positive_three_crossing_cycle.md).
Put
\[
 q=e^{\pi i/N},\quad D=N-1,\quad \eta=(-1)^D,\quad
 \kappa=q^{D^2/2},\quad H=M^*M,\quad
 S_j=\prod_{a=1}^j2\sin(\pi a/N),\quad S_0=1.
 \tag{1}
\]
Let
\[
 \gamma=MJM^3e_0,\qquad
 y_r=\frac{(-q)^{-r}S_r^2\gamma_r}{\gamma_0},\qquad
 \mu_{m,N}=e_0^*H^me_0.
 \tag{2}
\]
The proved endpoint estimate is
\(|\gamma_0|=N^{3/2}(1+O(N^{-1}))\), so (2) is defined for
all sufficiently large levels. All coefficient formulas below refer to
the full original matrices, including the normal directions at the
double physical roots.

We recall the established input from
[the next-crossing Fourier theorem](research_three_crossing_next_crossing_fourier.md).
For \(0\le x<1/2\), define
\[
 \begin{split}
 X(x)&=e^{-2\pi ix},\qquad R(x)=\sqrt{4/X(x)-3},\\
 \lambda(x)&=\frac{3-2X(x)+R(x)}2,\qquad
 \lambda_-(x)=\frac{3-2X(x)-R(x)}2,\\
 I(x)&=\int_0^x\log\lambda(t)\,dt,\qquad
 G(x)=\sqrt{\frac{\lambda(x)}{\lambda(x)-\lambda_-(x)}},\\
 J_0(x)&=\int_0^x\log(2\sin\pi t)\,dt,\\
 A(x)&=\Re I(x)-2J_0(x),\qquad
 B(x)=\Re I(x)-J_0(x).
 \end{split}
 \tag{3}
\]
The square root starts at \(R(0)=1\), the logarithm at zero, and
\(G(0)=1\). On the interior \(0<x<1/2\), one has
\(\Re\lambda>0\), \(\Im\lambda>0\), and
\(|\lambda|>|\lambda_-|\).
For every fixed \(b<1/2\), the actual input satisfies
\[
 y_r=G(r/N)e^{NI(r/N)}(1+O_b(N^{-1}))
                      \qquad(0\le r\le bN).
 \tag{4}
\]
At the other end, its already proved exponential rate is
\(B((D-r)/N)\). The two endpoint estimates, together with the
bounded transfer matrices in a small middle interval, control the
entire vector. No new choice of a dominant recurrence solution is
being made here.

The identity \(MHe_0=\kappa J\overline\gamma\), proved in
[the third-moment note](research_positive_three_crossing_cap_seed.md),
gives the following exact observation:
\[
 \boxed{\quad
 (H^2e_0)_k=
 \eta q^{-D(k+1)}\frac{\overline{\gamma_0}}{S_k}
       \sum_{r=0}^{D-k}q^{kr}
                \frac{S_{r+k}}{S_r^3}\,\overline{y_r}.
 \quad}
 \tag{5}
\]
Indeed the \((k,j)\)-entry of \(M^*\) is
\(\overline\kappa(-1)^jq^{-j(k+1)}S_j/(S_kS_{j-k})\).
Set \(r=D-j\), insert (2), and use
\(S_{D-r}=N/S_r\). The signs combine to \(\eta\), and the
remaining power of \(q\) is exactly that in (5).

## 2. Strict concavity of the absolute amplitude

We need a global maximum of the summands in (5), rather than only a
solution of its complex stationary equation. The next elementary
calculation supplies it.

**Lemma 1.** Both \(A\) and \(B\) are strictly concave on
\((0,1/2)\). The function
\[
 C(j)=
 \begin{cases}B(j),&0<j\le1/2,\\ A(1-j),&1/2\le j<1\end{cases}
 \tag{6}
\]
is continuously differentiable and strictly concave. Consequently
\[
 F(j,k)=J_0(j)-J_0(k)-J_0(j-k)+C(j)
                       \qquad(0<k<j<1)
 \tag{7}
\]
is strictly concave, including across \(j=1/2\).

*Proof.* Write
\[
 s=|R(x)|^2=\sqrt{25-24\cos(2\pi x)},\qquad
 h=\sqrt{\frac{7-s}{3(s+1)}}.
 \tag{8}
\]
As \(x\) increases from zero to \(1/2\), \(h\) strictly
decreases from one to zero. The identity
\(X=4/(R^2+3)\) gives
\(\lambda=X(1+R)^3/8\). Directly taking moduli yields, with
\(d=4\sin^2\pi x\),
\[
 d=\frac{4(1-h^2)}{(1+3h^2)^2},\qquad
 \frac{|\lambda|}{d}
   =\frac{\sqrt{(1+h)(1+3h^2)/2}}{1-h},\qquad
 \frac{|\lambda|}{\sqrt d}
   =\frac{\sqrt2(1+h)}{\sqrt{(1+3h^2)(1-h)}}.
 \tag{9}
\]
Since \(A'=\log(|\lambda|/d)\), its derivative with respect to
\(h\) is
\[
 \frac1{2(1+h)}+\frac{3h}{1+3h^2}+\frac1{1-h}>0.
 \tag{10}
\]
For \(B'=\log(|\lambda|/\sqrt d)\), the corresponding derivative is
\[
 \frac{3-7h+9h^2+3h^3}{2(1-h^2)(1+3h^2)}>0.
 \tag{11}
\]
The numerator is positive because \(9h^2-7h+3>0\) on the real
line. The strict decrease of \(h\) proves both concavity assertions.
At the joining point \(J_0(1/2)=0\), and
\(B'(1/2)=-A'(1/2)=\tfrac12\log2\). Thus (6) is \(C^1\).

For completeness, the Hessian of
\(E(j,k)=J_0(j)-J_0(k)-J_0(j-k)\) has negative diagonal
entries and determinant exactly \(\pi^2\) on the triangle
\(0<k<j<1\). This follows from the cotangent addition formula;
in particular
\(E_{jj}=\pi(\cot\pi j-\cot\pi(j-k))<0\).
Adding the concave function (6) preserves strict concavity on each
side and across their matching first derivatives. \(\square\)

For fixed \(k\), the derivative of (7) tends to \(+\infty\) at
\(j=k\) and to \(-\infty\) at \(j=1\). It therefore has a
unique interior maximum. This observation concerns the absolute
amplitude. It does not yet assert that its complex phase is stationary.

## 3. A real stationary observation

Let \(z_*\) be the unique negative real root of
\[
                         z^4-2z^2-z-1=0,
 \qquad -2<z_*<-1.
 \tag{12}
\]
Define
\[
 x_*=(2\pi)^{-1}\arccos(z_*/2),\qquad
 k_*=\pi^{-1}\arg\lambda(x_*),\qquad j_*=1-x_*.
 \tag{13}
\]
The argument in (13) lies in \((0,\pi/2)\). These constants satisfy
\(0<k_*<j_*<1\), with
\(x_*\in(.367,.368)\) and \(k_*\in(.214,.215)\).
In this note \(k_*\) is a real scaled observation coordinate, while
the subscript \(k\) in (5) is an integer.

For real \(x,k\) near this point put
\[
 \Psi(x,k)=\overline{I(x)}+J_0(x+k)-J_0(k)-3J_0(x)+i\pi kx.
 \tag{14}
\]
Complex derivatives in \(x\) use the holomorphic continuation
\(\overline{I(\overline x)}\). Set
\[
 F_*=\Re\Psi(x_*,k_*)
     =A(x_*)+J_0(x_*+k_*)-J_0(x_*)-J_0(k_*).
 \tag{15}
\]

**Lemma 2.** One has \(\Psi_x(x_*,k_*)=0\) and
\(\Re\Psi_{xx}(x_*,k_*)<0\). For the fixed observation \(k_*\),
the absolute amplitude has its unique global maximum at \(x_*\).

*Proof.* The complex stationary equation separates into
\[
 \arg\lambda(x)=\pi k,\qquad
 |\lambda(x)|\sin\pi(x+k)=4\sin^3\pi x.
 \tag{16}
\]
We verify the branch in (12), rather than choosing a root of an
eliminated polynomial without checking (16). Put
\(k(x)=\arg\lambda(x)/\pi\) and let \(E(x)\) denote the left
side of the second equation minus its right side. Near zero,
\(\lambda(x)=1+4\pi ix+O(x^2)\), so
\(E(x)=5\pi x+O(x^2)>0\). At \(x=1/2\), its limit is
\(\Re\lambda(1/2)-4=-3/2\). Hence it has a zero.

Write \(c=\cos(2\pi x)\), \(s_0=\sin(2\pi x)\), and
\(R=u+iv\), with \(u,v>0\). Equation (16) implies
\[
                  1+4c+u+\frac{s_0v}{1-c}=0.
 \tag{17}
\]
In particular any such root has \(2c<-1/2\).
Set \(Z=e^{2\pi ik}\). Substitution of
\(\lambda=dZ(1-X)/(Z-X)\) into its characteristic equation gives
\[
 f(X,Z)=(X-1)(X^2+1)Z^2+X^2(1-2X)Z+X^3=0.
 \tag{18}
\]
The reciprocal conjugate on the unit circles is
\(g(X,Z)=(1-X)(1+X^2)+(X-2)Z+Z^2=0\).
Their resultant in \(Z\) is
\[
 (X-1)^4X^4\left[(X+X^{-1})^4
               -2(X+X^{-1})^2-(X+X^{-1})-1\right].
 \tag{19}
\]
Thus every root of (16) in this interval has the negative root (12).
The quartic decreases strictly on \([-2,-1]\), changes sign there,
and has no zero on \([-1,0]\): writing \(z=-w\), its value there
is at most \(-w^2+w-1\le-3/4\). The existence just proved
therefore selects precisely (12) on the original branch of \(\lambda\).

Finally \(J_0(1-x)=-J_0(x)\), so
\(\Re\Psi(x,k)=F(1-x,k)\) when \(x<1/2\).
Lemma 1 proves strict negative real second derivative and the unique
global absolute maximum at this stationary point. \(\square\)

## 4. The coefficient survives the entire original sum

Choose an integer \(k_N\) nearest to \(Nk_*\), and put
\(\kappa_N=k_N/N\). Define
\[
 b_*=
 \overline{G(x_*)}
 \sqrt{\frac{\sin\pi(x_*+k_*)}
              {\sin\pi k_*\,\sin^3\pi x_*}}
 \frac1{\sqrt{-\Psi_{xx}(x_*,k_*)}}\ne0.
 \tag{20}
\]
The square root of \(-\Psi_{xx}\) has positive real part.

**Theorem 3.** Through all integer levels,
\[
 \boxed{\quad
 (H^2e_0)_{k_N}
  =\eta q^{-D(k_N+1)}\overline{\gamma_0}
       \frac{\sqrt\pi}{2N}\,b_*
       e^{N\Psi(x_*,\kappa_N)}
                         (1+O(N^{-1/2})).
 \quad}
 \tag{21}
\]
In particular this original coefficient is eventually nonzero and
\[
 \log|(H^2e_0)_{k_N}|=NF_*+\tfrac12\log N+O(1).
 \tag{22}
\]

*Proof.* In a fixed small neighborhood of \(x_*\), (4) and the
uniform sine-factorial expansion give
\[
 \frac{S_{r+k_N}}{S_{k_N}S_r^3}\overline{y_r}\,q^{k_Nr}
 =\frac{\overline{G(x)}}{(2N)^{3/2}}
   \sqrt{\frac{\sin\pi(x+\kappa_N)}
               {\sin\pi\kappa_N\,\sin^3\pi x}}
       e^{N\Psi(x,\kappa_N)}(1+O(N^{-1})),
 \qquad x=r/N.
 \tag{23}
\]
Here the factorial convention is
\(S_{Nx}=\sqrt{2N\sin\pi x}\,e^{NJ_0(x)}(1+O(N^{-1}))\)
on compact subintervals of \((0,1)\). All three indices in (23)
remain in such intervals. This fixes the prefactor in (21).

Since \(\kappa_N-k_*=O(N^{-1})\), the linear derivative
\(\Psi_x(x_*,\kappa_N)\) is \(O(N^{-1})\). On the scale
\(x=x_*+u/\sqrt N\), its contribution is \(O(u/\sqrt N)\).
The quadratic term has strictly negative real part. Gaussian
summation therefore contributes
\(\sqrt{2\pi N}/\sqrt{-\Psi_{xx}(x_*,k_*)}\), with relative
error \(O(N^{-1/2})\). For example, Taylor expansion on a fixed
small interval bounds the remainders by Gaussian moments; the
quadratic Gaussian sum differs from its integral exponentially
in \(N\), by its explicit Fourier transform. Multiplying by
\((2N)^{-3/2}\) gives \(\sqrt\pi/(2N)\).

We must also estimate every summand outside that neighborhood.
For the corresponding original \(j=D-r\), the two endpoint
profiles in (3)--(4), and uniform logarithmic factorial errors,
give the limiting absolute exponent (7). Rounding by \(1/N\)
changes this description by at most \(O(\log N/N)\), including
at a factorial endpoint. On closed sets away from \(j=1/2\),
Lemma 1 gives a strict gap below \(F_*\).

The small middle interval is controlled by the original bounded
transfer matrices used in the proof of the next-crossing theorem.
Starting at \(r/N=1/2-\epsilon+O(N^{-1})\), at most
\(2\epsilon N+O(1)\) transfers cost \(K^{2\epsilon N+O(1)}\)
for a fixed \(K\). The factorial factor in (5) is continuous
at that interval. As \(\epsilon\) decreases to zero, the resulting
upper exponent tends to \(F(1/2,k_*)<F_*\). Choose one sufficiently
small fixed \(\epsilon\). This gives a strict gap for the entire
middle band as well. These estimates are uniform for
\(\kappa_N-k_*=O(N^{-1})\).

There are only \(N\) summands. Their absolute complementary sum
is consequently exponentially smaller than the local term. This
proves (21) from the exact identity (5), with no phase assumption
on the discarded part. Equation (22) uses the proved value of
\(|\gamma_0|\) and the bounded quantity
\(N(\Re\Psi(x_*,\kappa_N)-F_*)\). \(\square\)

## 5. Improved lower bounds for all longer positive caps

Put \(w=2F_*\). The
[exact scalar certificate](../experiments/verify_positive_fourth_cap_observation.py)
and its [record](../repro/results/research-positive-fourth-cap-observation.json)
prove
\[
 F_*>\frac34,\qquad v<\frac{91}{100},\qquad
                    w>2v-c.
 \tag{24}
\]
Here \(v\) is the proved third-moment rate and \(c\) the second-moment
rate. The last inequality uses the independently proved \(c>8/25\):
\(2v-c<3/2<2F_*\). The approximate values
\(F_*=0.752103567624\ldots\) and \(w=1.504207135248\ldots\)
are only descriptions of these certified constants.

The fourth moment is the full positive norm
\(\mu_{4,N}=\|H^2e_0\|^2\). Retaining the single coefficient
in Theorem 3 proves, for some fixed \(c_4>0\),
\[
                         \mu_{4,N}\ge c_4 N e^{Nw}
                          \quad\text{for all sufficiently large }N.
 \tag{25}
\]
Increasing positive moment ratios now give, for every fixed \(m\ge4\),
\[
 \mu_{m,N}\ge
       \frac{\mu_{4,N}^{m-3}}{\mu_{3,N}^{m-4}}
 \ge c_m N^{3-m/2}
       e^{N[(m-3)w-(m-4)v]},\qquad c_m>0.
 \tag{26}
\]
The denominator uses the already proved upper asymptotic for
\(\mu_{3,N}\), not a conjectured fourth-moment equivalent.
By (24), this exponent strictly improves
\(v+(m-3)(v-c)\), the previous lower bound for these same
original capped words. The upper moment bound remains unchanged.

The separate [finite identity check](../experiments/check_positive_fourth_cap_observation.py)
constructs the crossing by multiplication and reduction in the original
Newton quotient. Its [record](../repro/results/research-positive-fourth-cap-exact-identity.json)
checks every coefficient of (5), in denominator-free form, for
\(N=2,\ldots,12\) and both crossing signs: 154 comparisons at
100 decimal digits. This checks the exact finite normalization;
the asymptotic and complementary-sum estimates are the written proof
of Theorem 3.

This proof uses a real stationary observation of the actual vector.
It does not replace the original coefficients by their absolute
values before summation. It also does not assert that the chosen
observation maximizes \(\|H^2e_0\|\); indeed it need not be a
joint maximum in \((j,k)\). Determining the sharp norm and its
geometric interpretation remains a further problem.
