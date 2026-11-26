# A nonzero profile selected by the original next-crossing source

The actual vector \(\gamma=MJ M^3e_0\) has a nonzero asymptotic
profile throughout each fixed compact part of either outer half
of its color range. The endpoint forcing selects the dominant
solution; no freely chosen solution of the classical recurrence
is substituted. A sine-factorial normalization removes the
apparent singularity at the initial color.

This note proves the profiles, with their complex amplitudes and
original scalar factors. A global maximum, a passage through the
middle modulus crossing, and a subsequent coherent contraction
are separate questions.

## 1. Exact source and regular endpoint coordinates

Set
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad D=N-1,\quad
 \kappa=q^{D^2/2},\quad
 S_j=\prod_{a=1}^j2\sin(\pi a/N),\quad
 d_j=4\sin^2(\pi j/N),\quad S_0=1.
 \tag{1}
\]
The original next-crossing calculation in
[the exact next-step source theorem](research_three_crossing_next_step_profile.md)
gives, for \(\alpha=M^3e_0\) and \(\gamma=MJ\alpha\),
\[
 q^{-1}d_{j+1}\gamma_{j+1}
 +[3-(1+Q^{-1})Q^{-j}]\gamma_j
 +q(1-Q^{-j})\gamma_{j-1}
       =\kappa^2\delta_{j0}.
 \tag{2}
\]
Missing endpoint terms are zero. In particular its retained
normalizations are
\[
 \gamma_0=\kappa\alpha_D,
 \qquad \gamma_D=N.
 \tag{3}
\]
The [full original three-crossing endpoint](research_three_crossing_full_coefficient_profile.md),
equations (5)--(6), supplies
\[
 \begin{split}
 \gamma_0&=\Omega_N N^{3/2}(1+O(N^{-1})),\\
 \Omega_N&=\kappa^4(-1)^Nq^{-1}\omega_N,\qquad
 \omega_N=\exp\!\left(i\pi\left[\frac14+
                         \frac1{4N}-\frac N{12}\right]\right).
 \end{split}
 \tag{4}
\]
Thus \(|\Omega_N|=1\) and \(\gamma_0\ne0\) at all sufficiently
large levels, including both parities.

Define the exact left endpoint coordinates
\[
 y_j=(-q)^{-j}S_j^2\frac{\gamma_j}{\gamma_0}.
 \tag{5}
\]
Dividing (2) by its retained factors gives
\[
 \begin{split}
 y_0&=1,\qquad y_1=2-Q^{-1}-\frac{\kappa^2}{\gamma_0},\\
 y_{j+1}&=b_N(j/N)y_j-h(j/N)y_{j-1},\qquad j\ge1,\\
 b_N(x)&=3-(1+e^{-2\pi i/N})e^{-2\pi ix},\\
 h(x)&=4\sin^2(\pi x)(1-e^{-2\pi ix}).
 \end{split}
 \tag{6}
\]
The coefficients of this recurrence are smooth at \(x=0\).
The actual forcing has become the explicit initial correction
\(\kappa^2/\gamma_0=O(N^{-3/2})\), rather than a discarded term.

## 2. The classical branch and its strict modulus gap

Fix \(b\) with \(0<b<1/2\). Write
\[
 X(x)=e^{-2\pi ix},\qquad b_0(x)=3-2X(x),
 \qquad b_1(x)=2\pi iX(x).
 \tag{7}
\]
Then \(b_N=b_0+N^{-1}b_1+O_b(N^{-2})\), with the same bound
after any fixed number of derivatives. The characteristic roots
of (6) at leading order are
\[
 \lambda(x)=\frac{3-2X(x)+\sqrt{4/X(x)-3}}2,
 \qquad
 \mu(x)=\frac{3-2X(x)-\sqrt{4/X(x)-3}}2.
 \tag{8}
\]
The square root is continued from its value \(1\) at zero. The
discriminant identity follows from
\(h=-(1-X)^3/X\). On \(0<x<1/2\), both \(3-2X\) and the
chosen square root have strictly positive real and imaginary
parts. Hence
\[
 |\lambda|^2-|\mu|^2
   =\operatorname{Re}\bigl((3-2X)\overline{\sqrt{4/X-3}}\bigr)>0.
 \tag{9}
\]
At zero, \(\lambda(0)=1\), \(\mu(0)=0\). The roots are distinct
everywhere on \([0,b]\), \(\lambda\) never vanishes, and therefore
\[
 \sup_{0\le x\le b}|\mu(x)/\lambda(x)|<1.
 \tag{10}
\]
All branch functions below are consequently smooth on this closed
interval. Use the logarithm of \(\lambda\) equal to zero at zero;
it is also its principal logarithm here.

## 3. Nonzero amplitude of the original solution

Define
\[
 r(x)=\frac{b_1(x)\lambda(x)-\mu(x)\lambda'(x)}
                    {\lambda(x)-\mu(x)},
 \quad
 a(x)=\lambda(x)^{-1/2}
             \exp\!\left(\int_0^x\frac{r(t)}{\lambda(t)}\,dt\right),
 \quad
 I(x)=\int_0^x\operatorname{Log}\lambda(t)\,dt.
 \tag{11}
\]
The square root of \(\lambda\) is one at zero. In particular
\(a(0)=1\), and \(a(x)\ne0\) throughout \([0,b]\).
In this actual recurrence the amplitude simplifies further:
\[
             a(x)=\sqrt{\frac{\lambda(x)}{\lambda(x)-\mu(x)}},
             \qquad a(0)=1.
 \tag{11a}
\]
Indeed \(b_1=b_0'/2=(\lambda'+\mu')/2\). The logarithmic
derivative of the definition in (11) is consequently
\[
 -\frac{\lambda'}{2\lambda}+\frac r\lambda
   =\frac{\lambda\mu'-\mu\lambda'}
                {2\lambda(\lambda-\mu)}
   =\frac12\left(\frac{\lambda'}\lambda
               -\frac{\lambda'-\mu'}{\lambda-\mu}\right),
\]
which proves (11a) with its displayed normalization.

**Theorem 1.** For every fixed \(b<1/2\), the actual source
coordinates (5) satisfy
\[
 \boxed{\displaystyle
 y_j=a(j/N)e^{NI(j/N)}(1+O_b(N^{-1}))
       \quad(0\le j\le\lfloor bN\rfloor).}
 \tag{12}
\]
The error is relative and uniform, and every displayed coordinate
is nonzero for all sufficiently large \(N\). Equivalently,
\[
 \gamma_j=\gamma_0(-q)^jS_j^{-2}
                    a(j/N)e^{NI(j/N)}(1+O_b(N^{-1})).
 \tag{13}
\]
For \(j+1\le\lfloor bN\rfloor\), the original consecutive ratio
also satisfies
\[
 \frac{\gamma_{j+1}}{\gamma_j}
 =\frac{-q}{d_{j+1}}
       \bigl(\lambda(j/N)+O_b(N^{-1})\bigr).
 \tag{14}
\]

*Proof.* Put \(\varepsilon=N^{-1}\) and
\(z_\varepsilon(x)=\lambda(x)+\varepsilon r(x)\).
Taylor expansion in a fixed neighborhood of \([0,b]\) gives
\[
 b_N(x)-\frac{h(x)}{z_\varepsilon(x-\varepsilon)}
             =z_\varepsilon(x)+O_b(\varepsilon^2).
 \tag{15}
\]
Indeed \(h=\lambda\mu\), so the first-order coefficient on the
left is
\(b_1+(\mu/\lambda)(r-\lambda')\); equation (11) says exactly
that this is \(r\). At the first step
\(r(0)=b_1(0)=2\pi i\). Equations (4) and (6) imply
\[
 y_1/y_0=z_\varepsilon(0)+O(\varepsilon^{3/2}).
 \tag{16}
\]

For completeness the following induction establishes the ratios
without presupposing that any later coordinate is nonzero.
Choose \(\rho<1\) larger than the supremum in (10).
There is a fixed sufficiently small neighborhood of the curve
\(\lambda([0,b])\) such that, whenever the two arguments are
close to the same \(\lambda(x)\),
\[
 \left|\frac{h(x)}{uv}\right|\le\rho.
 \tag{17}
\]
Increasing \(\rho\) slightly if necessary absorbs the
\(O(\varepsilon)\) difference between the neighboring sampled
curves. The neighborhood avoids zero. If
\(\tau_j=y_j/y_{j-1}\) is defined and close to
\(z_\varepsilon((j-1)\varepsilon)\), equations (6), (15), and
\[
 \left(b_N-\frac h u\right)
       -\left(b_N-\frac h v\right)=\frac{h(u-v)}{uv}
\]
show that the next ratio is defined, stays in that neighborhood,
and obeys
\[
 |\tau_j-z_\varepsilon((j-1)\varepsilon)|
       \le C_b\varepsilon^2
                    +C_b\varepsilon^{3/2}\rho^{j-1}.
 \tag{18}
\]
Start with (16), and use the geometric series to close this
induction. In particular every \(y_j\) under consideration is
nonzero. Since \(|z_\varepsilon|\) is bounded below, summing the
logarithms of its relative ratio errors in (18) gives
\[
 y_j=\prod_{l=0}^{j-1}z_\varepsilon(l\varepsilon)
                                          (1+O_b(\varepsilon)).
 \tag{19}
\]
The sum of the \(O(\varepsilon^2)\) errors is
\(O(\varepsilon)\); the geometrically decaying initial error
contributes only \(O(\varepsilon^{3/2})\).

Now
\(\operatorname{Log}z_\varepsilon
 =\operatorname{Log}\lambda+\varepsilon r/\lambda
 +O_b(\varepsilon^2)\). Euler summation of these smooth
functions, uniformly for every upper index \(j\), yields
\[
 \sum_{l=0}^{j-1}\operatorname{Log}z_\varepsilon(l\varepsilon)
 =NI(x)-\tfrac12\operatorname{Log}\lambda(x)
       +\int_0^x r(t)/\lambda(t)\,dt+O_b(N^{-1}),
 \quad x=j/N.
 \tag{20}
\]
Here \(\operatorname{Log}\lambda(0)=0\). Exponentiating proves
(12); (13)--(14) follow from the exact scaling (5).
\(\square\)

On any compact interval \([a,b]\subset(0,1/2)\), the standard
full sine-factorial expansion
\(S_j^2=2N\sin(\pi j/N)e^{2N\mathcal J(j/N)}(1+O_{a,b}(N^{-1}))\),
where \(\mathcal J(x)=\int_0^x\log(2\sin\pi t)\,dt\), turns (13)
into the explicit bulk profile
\[
 \gamma_j=\Omega_N(-q)^j N^{1/2}
     \frac{a(x)}{2\sin\pi x}
     e^{N[I(x)-2\mathcal J(x)]}(1+O_{a,b}(N^{-1})).
 \tag{21}
\]
Thus the exponential rate at these actual colors is
\(\operatorname{Re}I(x)-2\mathcal J(x)\), with a nonzero
amplitude, not merely an upper envelope.

## 4. The actual opposite endpoint

Write \(F_r=(Q;Q)_r\) and retain the exact right endpoint scaling
\[
 p_r=(-1)^r q^r F_r\frac{\gamma_{D-r}}N.
 \tag{22}
\]
The same original equation (2), read from its other end, gives
\[
 \begin{split}
 p_0&=1,\qquad p_1=2-Q,\\
 p_{r+1}&=[3-(1+Q)Q^r]p_r-d_r(1-Q^r)p_{r-1}.
 \end{split}
 \tag{23}
\]
This is the complex conjugate of (6) without the small initial
source correction. Its coefficients and its nonzero endpoint
come from (2)--(3), not a new terminal boundary condition.
The proof of Theorem 1 applies by conjugation; the initial error
in (16) is now \(O(N^{-2})\). Consequently
\[
 p_r=\overline{a(r/N)}e^{N\overline{I(r/N)}}
                      (1+O_b(N^{-1}))
        \quad(0\le r\le\lfloor bN\rfloor).
 \tag{24}
\]
The exact finite-product phase
\(F_r=(-i)^r q^{r(r+1)/2}S_r\) then gives
\[
 \gamma_{D-r}=N(-i)^r q^{-r(r+3)/2}S_r^{-1}
       \overline{a(r/N)}e^{N\overline{I(r/N)}}
                         (1+O_b(N^{-1})).
 \tag{25}
\]
In particular its bulk rate is
\(\operatorname{Re}I(x)-\mathcal J(x)\), not the left-hand
rate in (21). Replacing the finite product by its absolute value
before deriving (25) would discard the displayed original phase.

Every formula here has the conjugate version for the negative
crossing convention. The conclusions hold at all sufficiently
large integer levels of either parity. They do not assert a
simultaneous limit in a growing word length or a nonzero value
after the remaining coherent boundary contraction.

## 5. Exact normalization checks

The independent original-matrix checker
[check_three_crossing_next_crossing.py](../experiments/check_three_crossing_next_crossing.py)
and its [saved result](../repro/results/research-three-crossing-next-crossing.json)
verify the underlying finite recurrence and endpoint normalizations.
The asymptotic statements (12)--(25) follow from the preceding
uniform Riccati proof, not from those finite checks.
