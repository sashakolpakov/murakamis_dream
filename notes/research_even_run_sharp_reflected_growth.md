# Sharp growth of every reflected even crossing run

Research note, 3 November 2026.

For each fixed even crossing power, the complete original reflected
scalar has a sharp exponential rate. The initially largest backward
mode is strictly dominant whenever its growth exceeds the sine
factorial normalization. Its normalized modulus crosses one exactly
once before the middle colors. The previously proved endpoint data
select this mode with a nonzero coefficient. The original low-color
bound and middle contraction then give the matching global upper
bound.

This is an asymptotic statement for the original positive reflected
closing scalar, at all sufficiently large integer levels and both
parities. The volume identification is proved separately in
[the reflected even knot theorem](research_reflected_even_kashaev_volume_theorem.md),
using this rate, the original geometric periods, and an absolute
regulator comparison. A free-boundary packet and noncancellation
of a different signed closing word are not conclusions of this note.

## 1. Original source and the classical branches

Fix \(k\ge2\). Retain the original algebra, crossing matrix \(M\),
Frobenius trace \(\phi_N\), and turn \(T\). Set
\[
 \begin{split}
 \alpha_{k,N,j}&=(M^{2k}e_0)_j,\qquad D=N-1,\\
 \mathcal E_{k,N}
   &=\phi_N(R^{-2k}T(R^{2k}))
     =\sum_{j=0}^{D}|\alpha_{k,N,j}|^2 .
 \end{split}                                                    \tag{1}
\]
The equality is the original reflected pairing, including its
carrier. Opposite powers supply the conjugation; no absolute-value
replacement of a coherent source is made.

Let \(T_k\) be path adjacency and put
\[
 J_k(X)=T_k+E_{kk}+XE_{11},\qquad
 H(\theta)=2\cos\theta\,I-T_k-e^{-i\theta}E_{11}-E_{kk},
 \qquad \delta(\theta)=2-2\cos\theta .
 \tag{2}
\]
Use the holomorphic simple eigenvalues from
[the marked-kernel theorem](research_even_run_simple_spectrum_and_marked_kernel.md):
\[
 \mu_j(1)=2\cos(j\pi/k),\qquad 0\le j<k.
 \tag{3}
\]
The eigenvalues of \(H(\theta)\) are
\(2\cos\theta-\mu_j(e^{-i\theta})\).
We denote by \(\lambda_*(\theta)\) the branch with initial value
\[
                 \lambda_*(0)=4\cos^2(\pi/(2k)).
 \tag{4}
\]
It corresponds to \(\mu_{k-1}\). All statements about moduli can
equivalently use the conjugate parameter \(X=e^{i\theta}\).

The simple-spectrum theorem is used with its proved sector
information. For \(X=e^{i\theta}\), \(0<\theta\le\pi/2\), write
\[
 \mu=-(z+z^{-1}),\qquad z=e^{-\eta+i\varphi},\qquad \eta>0.
 \tag{5}
\]
The sector for the branch (4) is
\[
            \frac{\pi}{2k}<\varphi_*<\frac{\pi}{k},
 \tag{6}
\]
and every other branch has strictly larger \(\varphi\).
These assertions include multiplicity and branch labels: they
follow by putting \(z\) equal to minus the inner Joukowski root
in the disjoint sectors of that theorem.

## 2. A modulus comparison on the whole first quarter

**Lemma 1.** For \(0<\theta\le\pi/2\), every eigenvalue
\(\lambda\) of \(H(\theta)\), other than \(\lambda_*(\theta)\),
satisfies
\[
 \begin{cases}
 |\lambda|<|\lambda_*|,
                      &|\lambda_*|\ge\delta(\theta),\\
 |\lambda|<\delta(\theta),
                      &|\lambda_*|<\delta(\theta).
 \end{cases}                                                    \tag{7}
\]
In particular a modulus switch away from the initial largest
branch can occur only where every normalized modulus is below one.

*Proof.* Put \(c=\cos\theta\), \(s=\sin\theta\). The Chebyshev
characteristic equation, in the coordinate (5), is
\[
      z^{2k}=\frac{1+Xz}{z+X},\qquad X=e^{i\theta}.
 \tag{8}
\]
Taking absolute values gives exactly
\[
 \tanh(2k\eta)
       =\frac{s\sin\varphi}{\cosh\eta+c\cos\varphi}.
 \tag{9}
\]
For every \(0<\varphi<\pi\), (9) determines a unique
\(\eta=\eta_\theta(\varphi)>0\): after multiplication by
the positive denominator, its left side is strictly increasing
from zero to infinity as \(\eta\) increases. This also gives
smooth dependence on \(\varphi\). The endpoint limits at
\(\varphi=0,\pi\) are zero.

Write
\[
 C=\cosh\eta,\quad S=\sinh\eta,\quad v=\cos\varphi,\quad
 t=\sin\varphi,\quad
 \Delta=(v+cC)^2+s^2S^2>0.
 \tag{10}
\]
Along this curve the squared modulus is
\[
 g(\varphi)=\frac{|2c-\mu|^2}{4}
              =c^2+2cCv+v^2+S^2.
 \tag{11}
\]
Implicit differentiation of (9) gives
\[
 \eta'=\frac{s(Cv+c)}{2k\Delta+stS},\qquad
 g'=-\frac{2\Delta}{2k\Delta+stS}
                   [\,2kt(v+cC)-sSv\,].
 \tag{12}
\]
Here the identity
\((C+cv)^2-s^2t^2=\Delta\) accounts for the denominator;
expansion of (11) gives the second formula.

First suppose \(0<\varphi\le\pi/2\). Since
\(\tanh\eta\le\tanh(2k\eta)\), (9) gives \(S\le st\).
Thus the bracket in (12) is bounded below by
\[
             t[(2k-s^2)v+2kcC].
 \tag{13}
\]
It is strictly positive when \(v>0\). Consequently \(g\)
strictly decreases on \((0,\pi/2)\). By (6), the branch
\(\lambda_*\) has the largest modulus among all roots in
this half of the curve, and
\(g(\pi/2)<|\lambda_*|^2/4\).

We next prove that \(g\) has no interior maximum on
\([\pi/2,\pi]\). Put \(u=-v\ge0\), \(y=u/C\), and
\[
                r(\eta)=\frac{\tanh\eta}{\tanh(2k\eta)}.
 \tag{14}
\]
This function strictly increases for \(\eta>0\):
its logarithmic derivative is
\(2/\sinh(2\eta)-4k/\sinh(4k\eta)>0\).
Using (9), the sign-controlling bracket in (12), divided
by the positive number \(tC\), becomes
\[
             2k(c-y)+\frac{s^2y\,r(\eta)}{1-cy}.
 \tag{15}
\]
For \(y\le c\) it is positive. On \(y>c\), formula (12)
for \(\eta'\) gives \(\eta'<0\), since
\(Cv+c=c-C^2y<0\). Hence \(y\) increases strictly and
\(r(\eta)\) decreases strictly along this part of the curve.
When \(c>0\), the competing function
\[
 F_c(y)=\frac{2k(y-c)(1-cy)}{s^2y}
        =\frac{2k}{s^2}[1+c^2-c(y+y^{-1})]
 \tag{16}
\]
strictly increases for \(c<y<1\). The expression (15)
has the sign of \(r(\eta)-F_c(y)\) there. Thus its sign can
change at most once, from positive to negative. The region
\(y>c\) cannot be exited after entry, because \(y'>0\)
throughout it.
If \(c=0\), (15) is instead \(y[r(\eta)-2k]<0\) for
\(y>0\). In either case \(g'\) can change at most from
negative to positive, not the reverse.
The endpoints in (11) consequently give, strictly for
\(\pi/2<\varphi<\pi\),
\[
      g(\varphi)<
                  \max\{g(\pi/2),(1-c)^2\}.
 \tag{17}
\]
The strictness follows from the strict inequalities just proved:
there is no constant interval or interior maximum.
At \(\varphi=\pi\) the virtual endpoint has \(\eta=0\),
so \(g(\pi)=(1-c)^2=\delta(\theta)^2/4\);
it is not an eigenvalue coordinate.

All actual branches occur at interior values of \(\varphi\).
The strict decrease on the first half and (17) on the second,
together with (6), prove (7). \(\square\)

## 3. The unique unit-growth crossing

**Lemma 2.** There is a unique
\(\theta_k\in(0,\pi/2)\) for which
\[
                  |\lambda_*(\theta_k)|=\delta(\theta_k).
 \tag{18}
\]
The left side is greater than the right side before this point
and smaller after it on \((0,\pi/2]\).
At \(\theta_k\), every other normalized eigenvalue has modulus
strictly less than one.

*Proof.* We first prove uniqueness, without assuming monotonicity
of \(|\lambda_*|\). Put \(a=\eta-i\varphi\) in (5).
Equation (8) is equivalently
\[
 X=-\frac{\sinh((k+\tfrac12)a)}
          {\sinh((k-\tfrac12)a)},\qquad
 \frac{2\cos\theta-\mu}{\delta(\theta)}
          =-\frac{\sinh^2(a/2)}{\sinh^2(ka)} .
 \tag{19}
\]
All denominators are nonzero in the sector (6), since \(\eta>0\).
The conditions \(|X|=1\) and unit normalized modulus in (19)
are precisely
\[
 \begin{split}
 F(\eta,\varphi)
   &=\cosh(2k\eta)-\cos(2k\varphi)-\cosh\eta+\cos\varphi=0,\\
 B(\eta,\varphi)
   &=\sinh(2k\eta)\sinh\eta
                         +\sin(2k\varphi)\sin\varphi=0.
 \end{split}                                                    \tag{20}
\]

In the sector (6), \(F\) is strictly increasing with
\(\eta>0\), and tends to infinity. At \(\eta=0\) its sign
is the sign of
\(\cos\varphi-\cos(2k\varphi)\).
Thus a positive solution exists exactly when
\[
        \varphi_0:=\frac{2\pi}{2k+1}<\varphi<\frac{\pi}{k}.
 \tag{21}
\]
It defines a continuous function \(\eta_c(\varphi)\), zero at
\(\varphi_0\), positive afterward, and strictly increasing:
\[
 F_\eta=2k\sinh(2k\eta)-\sinh\eta>0,\qquad
 F_\varphi=2k\sin(2k\varphi)-\sin\varphi<0 .
 \tag{22}
\]
Smoothness is only needed away from the left endpoint.

Along this critical curve, \(B\) strictly increases. Indeed
\(B_\eta>0\), while, writing
\(\beta=2\pi-2k\varphi\), one has \(0\le\beta\le\varphi\le\pi/2\)
on the interval (21), with its right endpoint included. Hence
\[
 \begin{split}
 B_\varphi
   &=2k\cos\beta\sin\varphi-\sin\beta\cos\varphi\\
   &\ge(2k-1)\cos\varphi\sin\varphi>0
                       \qquad(\varphi<\pi/2).
 \end{split}                                                    \tag{23}
\]
At the only remaining endpoint, \(k=2,\varphi=\pi/2\),
the exact expression is \(B_\varphi=2k>0\).
At the two endpoints of the critical curve,
\[
 B(0,\varphi_0)=-\sin^2\varphi_0<0,\qquad
 B(\eta_c(\pi/k),\pi/k)>0.
 \tag{24}
\]
Therefore (20) has exactly one solution in (6).
Every actual crossing of the branch (4) gives such a solution,
and (19) determines \(X\) uniquely from it. There can be at
most one crossing in \(0<\theta\le\pi/2\).

Existence on this interval follows from two established endpoints.
At zero, \(|\lambda_*|/\delta\) tends to infinity by (4).
At \(\pi/2\), the frozen matrix
\(H(\pi/2)/\delta(\pi/2)\) is strictly Schur stable by
Lemma 1 of
[the middle-color contraction theorem](research_even_run_middle_color_contraction.md).
Continuity gives a crossing strictly before \(\pi/2\).
The uniqueness just proved then fixes the two strict signs.
Finally Lemma 1 gives strict separation from all other modes
at the crossing. \(\square\)

## 4. The exact sharp logarithmic rate

Define the original sine entropy and the actual dominant-branch
action by
\[
 \begin{split}
 J(x)&=\int_0^x\log(2\sin\pi t)\,dt,\qquad
 x_k=\frac{\theta_k}{2\pi}\in(0,1/4),\\
 B_k(x)&=\int_0^x\log|\lambda_*(2\pi t)|\,dt-2J(x),\\
 E_k(x)&=\int_0^x\log\rho(H(2\pi t))\,dt-2J(x).
 \end{split}                                                    \tag{25}
\]
The branch \(B_k\) is used below on a neighborhood of \([0,x_k]\),
where its logarithm has no zero singularity.

**Theorem 3.** The original reflected scalar (1) satisfies
\[
 \boxed{\qquad
 \lim_{N\to\infty}\frac1N\log\mathcal E_{k,N}
       =2B_k(x_k)
       =2\max_{0\le x\le1/4}E_k(x)>0 .
 \qquad}                                                       \tag{26}
\]
The maximum of \(E_k\) on this interval is unique.
The limit is through all integer levels, not a selected parity
or residue class. The same conclusion holds with the two
crossing signs reversed.

*Proof.* Lemmas 1--2 show
\[
 \begin{array}{ll}
 \rho(H(\theta))=|\lambda_*(\theta)|>\delta(\theta),
                                   &0<\theta<\theta_k,\\
 \rho(H(\theta_k))=\delta(\theta_k),&\\
 \rho(H(\theta))<\delta(\theta),&
                                   \theta_k<\theta\le\pi/2 .
 \end{array}                                                    \tag{27}
\]
Since \(2J'(x)=\log\delta(2\pi x)\), \(E_k\) strictly increases
to \(x_k\) and strictly decreases afterward on the first quarter.
It equals \(B_k\) up to \(x_k\).
The integrable singularity at zero gives \(E_k(0)=0\);
its strict increase proves that the maximum is positive.

The complete original endpoint vector has a nonzero leading
projection onto the mode (4), at every sufficiently large level,
by Theorem 1 of
[the backward-source theorem](research_even_run_backward_source_growth.md).
This is the fixed Gaussian endpoint calculation with every original
normal and its exact carrier retained. Lemma 1 gives strict
dominance throughout \(0\le\theta\le\theta_k\).
At \(\theta_k\) the gap is still strict, by Lemma 2.
Simplicity and compactness therefore extend a nonzero dominant
branch and a uniform relative modulus gap to some fixed interval
\([0,\theta_k+\varepsilon_k]\).

All hypotheses of the actual coefficient proof, Theorem 2 of
the cited backward-source note, now hold on this larger interval.
Its proof uses the resolved nonzero endpoint mode, contraction
of the complementary modes after \(O_k(\log N)\) initial steps,
and the uniformly nonzero last-coordinate observation.
It therefore gives, uniformly for \(h/N\) in any compact
subinterval of \((0,x_k+\varepsilon_k/(2\pi))\),
\[
        \log|\alpha_{k,N,D-h}|
                        =N B_k(h/N)+O_k(\log N).
 \tag{28}
\]
In particular choose \(h\) to be an integer nearest \(Nx_k\).
This single nonnegative summand of (1) proves the lower bound
in (26). No arbitrary dominant initial vector has been substituted.

For the upper bound use Corollary 2 and equation (19) of
[the original low-color estimate](research_original_low_color_bound.md).
The exact unit-modulus physical values bound the entire low-color
quarter by \(O(N)\) in squared norm; the full middle contraction
bounds all remaining middle colors by a fixed multiple of the
upper-quarter observation window. Hence the complete scalar has
the upper bound
\[
 \limsup_{N\to\infty}\frac1N\log\mathcal E_{k,N}
                       \le2\max_{0\le x\le1/4}E_k(x).
 \tag{29}
\]
The spectral-radius product bound used here permits arbitrary
modulus switches and retains every original color. Equation (27)
identifies its maximum, so (29) equals the lower bound from (28).
This proves the limit and uniqueness assertion.
Entrywise conjugation handles the reversed signs. \(\square\)

For \(k=1\) the already known exact source
\(|(M^2e_0)_j|=S_j\) gives its sharp reflected factorial rate
directly. The new argument covers every fixed \(k\ge2\).

The number in (26) is specified by a unique real crossing of
the original classical transfer and an explicit branch integral.
No geometric identification of this spectral action is needed
for the proof. That identification is supplied by
[the spectral transgression](research_reflected_even_spectral_volume_transgression.md)
and [the original geometric point](research_even_reflected_run_geometric_point.md).
Retaining a boundary variable through a subsequent short turn
remains a separate source problem.
