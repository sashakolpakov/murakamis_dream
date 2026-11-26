# The original three-boundary source on the real unit cube

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The centered multiplication tensor has a nonzero leading
asymptotic on every compact subset of the real cube \((-1,1)^3\).
Both its phase and amplitude are explicit. This is an estimate
of the entire original three-boundary source, with its first
Casimir normals and original closing retained.

The source selects two unit Fourier charges. Their contributions
add. The zero-charge integral vanishes exactly, and all remaining
charges, including their endpoint terms, have a summable uniform
bound. No geometric cycle coefficient is assigned by hand.

The result concerns real generating parameters. It does not assert
a fixed complex neighborhood, a connection across Stokes regions,
or a volume identity after arbitrary short fillings.

## 1. Statement with the original scalar factors

Fix \(N\ge2\), and set
\[
 d=N-1,\quad \eta=(-1)^d,\quad
 q=e^{\pi i/N},\quad Q=q^2,\quad
 \kappa=q^{d^2/2},\qquad D_N(t)=1-\eta t^N .
 \tag{1}
\]
All powers \(q^\alpha\) mean \(e^{\pi i\alpha/N}\).
Use the original full algebra
\(\mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2)\), the positive
crossing \(R\), and the original Frobenius row \(\phi\).
Here \(T_N(\cos\theta)=\cos(N\theta)\).
The initialized centered source is
\[
 \mathcal C_N(\mathbf t)
   =\sum_{a,b,c=0}^{d}C_{abc}t_1^at_2^bt_3^c
   =N^{-3/2}\phi\!\left(R^3
                       \prod_{\nu=1}^3G_N(t_\nu;z)\right).
 \tag{2}
\]
This is the same polynomial as in the finite
\({}_6\phi_5\) source identity. In particular its closing is
\(\phi\), rather than a norm or an ordinary spectral trace.

For real \(|t_\nu|<1\), define
\[
 \begin{aligned}
 \Psi(\mathbf t)=-\frac{\pi}{12}
 +\frac1{2\pi}\left[
    \sum_{\nu=1}^3\operatorname{Li}_2(-t_\nu)
       +\operatorname{Li}_2(-t_1t_2t_3)
       -\sum_{\mu<\nu}\operatorname{Li}_2(t_\mu t_\nu)\right],\\
 B(\mathbf t)=
             \prod_{\mu<\nu}(1-t_\mu t_\nu)^{-1/2}.
 \end{aligned}
 \tag{3}
\]
Every square root is positive. The dilogarithm is the real
analytic function obtained from
\(\operatorname{Li}_2(x)=\sum_{n\ge1}x^n/n^2\) on
\((-1,1)\). Thus \(\Psi\) is real and \(B>0\) throughout
this cube.

**Theorem.** For every \(0<\rho<1\), uniformly for
\(\mathbf t\in[-\rho,\rho]^3\),
\[
 \boxed{\quad
 \mathcal C_N(\mathbf t)=
 (-1)^N\kappa^3
       e^{\,i\pi/4-3\pi i/(4N)}
 \left[\prod_{\nu=1}^3D_N(t_\nu)\right]
 B(\mathbf t)e^{\,iN\Psi(\mathbf t)}
                         (1+O_\rho(N^{-1})).
 \quad}
 \tag{4}
\]
The sequence includes both parities and composite levels.
Consequently the actual polynomial is nonzero on that entire
real compact cube for all sufficiently large \(N\). The
normalizing factors \(D_N\) and the crossing phase have been
displayed rather than reset.

## 2. A smooth interpolation with calibrated physical normals

Put \(p=Q^{-1}\), and write \(W_n(z)=2T_n(z/2)\).
The full generating-section theorem supplies the explicit unit
\[
 U_N(t,z)=\exp\left\{\sum_{n=1}^{N-1}
  \frac{(-1)^{n+1}(W_n(z)-2q^{-n})}{n(p^n-1)}\,t^n\right\}.
 \tag{5}
\]
At every physical node
\(c_j=2\cos\theta_j\), \(\theta_j=(2j+1)\pi/N\),
it proves
\[
 \left|G_N/U_N-1\right|
   +\left|\partial_z(G_N/U_N)\right|
                       \le C_\rho N^2\rho^N .
 \tag{6}
\]
The derivative is required at double nodes; at the odd simple
node \(-2\) only the value is used. Every quantity in (6)
is evaluated at the actual finite polynomial's physical data.
Its proof includes the central correction in the root equation.

For use between sampling points, define
\[
 \begin{aligned}
 b(t,z)&=1+zt+t^2,\qquad A(t,z)=b(t,z)^{-1/2},\\
 \Phi(t,z)&=\frac{
   \operatorname{Li}_2(-wt)+\operatorname{Li}_2(-w^{-1}t)
                         -2\operatorname{Li}_2(-t)}{2\pi i},
                  \qquad z=w+w^{-1}.
 \end{aligned}
 \tag{7}
\]
The branches are analytic at \(t=0\), with \(A(0,z)=1\).
On real \(t\) and \(z=2\cos\theta\), the expression for
\(\Phi\) is independent of choosing \(w=e^{i\theta}\)
or \(w^{-1}\), is purely imaginary, and
\(A(t,2\cos\theta)>0\).

We need control of (5) at all real angles, rather than an
unproved continuation of (6) away from the nodes.
The logarithm of \(U_N\) below means its displayed exponent
in (5), and the other logarithms are anchored at \(t=0\).

**Lemma 1.** For every fixed integer \(k\ge0\), uniformly for
real \(|t|\le\rho\),
\[
 \left\|\log U_N(t,2\cos\theta)
          -N\Phi(t,2\cos\theta)-\log A(t,2\cos\theta)
                     \right\|_{C^k([0,2\pi])}
                                  \le C_{\rho,k}/N .
 \tag{8}
\]

**Proof.** At \(z=2\cos\theta\), \(W_n(z)=2\cos(n\theta)\).
For \(n\le N/2\), expand the scalar denominator in (5):
\[
 \frac1{e^{-2\pi in/N}-1}
       =-\frac{N}{2\pi in}-\frac12+O(n/N).
 \tag{9}
\]
Together with \(q^{-n}=e^{-\pi in/N}\), this gives the
coefficient identity
\[
 \frac{(-1)^{n+1}(2\cos n\theta-2q^{-n})}
                            {n(p^n-1)}
 =(-1)^n\left[
   \frac{N(2\cos n\theta-2)}{2\pi i n^2}
                       +\frac{\cos n\theta}{n}\right]
                      +E_{N,n}(\theta),
 \tag{10}
\]
where
\(\|\partial_\theta^kE_{N,n}\|_\infty
      \le C_k(1+n)^k/N\).
The expansions are uniform up to \(n=N/2\), since their
next denominator pole is at \(2\pi\).

For \(N/2<n<N\), use
\[
 |p^n-1|\ge c(N-n)/N .
 \tag{11}
\]
The \(k\)-th angle derivatives of those coefficients are bounded
by \(C_kN^k/(N-n)\). Their \(t^n\) tails are exponentially
small, up to a polynomial in \(N\), on \(|t|\le\rho\).
The same is true for the missing tails \(n\ge N\) of
the two main series in (10).
Summing (10) therefore has \(C^k\) error \(O(N^{-1})\).
Its two main series are exactly \(N\Phi\) and \(\log A\),
by the power series for \(\operatorname{Li}_2\) and the logarithm.
This proves (8). \(\square\)

For \(\mathbf t\in[-\rho,\rho]^3\), set
\[
 A_N(\theta)=
    \prod_{\nu=1}^3U_N(t_\nu,2\cos\theta)
       \exp\left\{-N\sum_{\nu=1}^3
                              \Phi(t_\nu,2\cos\theta)\right\}.
 \tag{12}
\]
For every fixed \(k\), Lemma 1 gives
\[
 A_N(\theta)=A_*(\theta)+O_{C^k,\rho}(N^{-1}),\qquad
 A_*(\theta)=\prod_{\nu=1}^3
                   (1+2t_\nu\cos\theta+t_\nu^2)^{-1/2}.
 \tag{13}
\]
All these amplitudes have uniform \(C^k\) bounds.
They are exactly invariant under \(\theta\mapsto2\pi-\theta\).

## 3. The source itself removes the zero Fourier charge

For any polynomial \(f\), the paired residue formula for the
original Frobenius source is equivalently
\[
 \phi(f)=(-1)^N\sum_{j=0}^{d}
       \left.\frac d{d\theta}
                  \{\sin\theta\,f(2\cos\theta)\}
                               \right|_{\theta=\theta_j}.
 \tag{14}
\]
Indeed each paired node gives
\((-1)^N[c f(c)+(c^2-4)f'(c)]\). At odd \(N\),
the point \(\theta=\pi\) contributes \(f(-2)\), as required.
Thus (14) includes the odd simple node.

Introduce the smooth angular interpolation
\[
 \chi_N=q^{d^2/4},\qquad
 r_N(\theta)=\chi_N
                   e^{\,iN(\theta-\pi)^2/(4\pi)} .
 \tag{15}
\]
At every \(\theta_j\), its value is the actual \(R(c_j)\).
At the double nodes its first derivative also gives the actual
Casimir derivative:
\[
 R(c_j)=\kappa(-1)^jq^{j(j+1)},\qquad
 \frac{R'(c_j)}{R(c_j)}
                     =\frac{i(d-2j)}{4\sin\theta_j}.
 \tag{16}
\]
The second identity is required only when \(\sin\theta_j\ne0\).
The odd simple node uses its value alone.
This verifies the interpolation at the full Hermite data.
It is not asserted that (15) equals the canonical crossing
polynomial between the sampling points.

We may factor the scalar \(\prod_\nu D_N(t_\nu)\) out of
(2) exactly. Replacing each \(G_N/D_N\) by \(U_N\) in the
remaining physical Hermite data has exponentially small source
error. To check the scale, (6), \(D_N=1+O(\rho^N)\), and
the generating-section normal estimate give, uniformly at the
nodes, bounded values of \(U_N\) and derivatives \(O_\rho(N)\).
The crossing has unit nodal values and first derivatives
\(O(N^2)\) by (16). A product difference therefore has value
error \(O_\rho(N^2\rho^N)\) and derivative error
\(O_\rho(N^4\rho^N)\). Formula (14), or its paired version,
bounds its source by \(O_\rho(N^5\rho^N)\).

Define the real phase
\[
 \sigma(\theta)=\frac{3(\theta-\pi)^2}{4\pi}
              +\frac1i\sum_{\nu=1}^3\Phi(t_\nu,2\cos\theta)
 \tag{17}
\]
and the amplitude \(a_N(\theta)=\sin\theta\,A_N(\theta)\).
Equations (12)--(17) consequently reduce the actual source to
\[
 \mathcal C_N=
 \left[\prod_\nu D_N(t_\nu)\right]
   N^{-3/2}(-1)^N\chi_N^3
       \sum_{j=0}^{d}
         \left.\frac d{d\theta}
               \{a_N(\theta)e^{iN\sigma(\theta)}\}
                                  \right|_{\theta=\theta_j}
               +O_\rho(N^4\rho^N).
 \tag{18}
\]

Put \(L_N(\theta)=a_N(\theta)e^{iN\sigma(\theta)}\).
Its endpoint values are zero. Its first derivatives agree at
\(0\) and \(2\pi\), since \(A_N\) is reflection-even and
\(\sigma(0)=\sigma(2\pi)\). Hence \(L_N'\), regarded as a
periodic continuous function, has absolutely summable Fourier
coefficients: two integrations by parts give the usual
\(O(m^{-2})\) bound, allowing the jump of its first derivative
at the seam. This justification is for each fixed \(N\).
The finite midpoint sampling identity is therefore exact:
\[
 \sum_{j=0}^{d}L_N'(\theta_j)
  =\frac{N}{2\pi}\sum_{\ell\in\mathbb Z}(-1)^\ell
          \int_0^{2\pi}L_N'(\theta)e^{-i\ell N\theta}\,d\theta
  =\frac{iN^2}{2\pi}\sum_{\ell\ne0}(-1)^\ell\ell I_{\ell,N},
 \tag{19}
\]
where
\[
 I_{\ell,N}=\int_0^{2\pi}
             a_N(\theta)e^{iN(\sigma(\theta)-\ell\theta)}\,d\theta .
 \tag{20}
\]
The last equality integrates by parts using \(L_N(0)=L_N(2\pi)=0\).
In particular the zero-charge integral is zero exactly.
No physical node, including the odd simple node, was deleted.
These Fourier labels come from the midpoint sampling formula;
they are not filling coefficients or peripheral charges.

## 4. All nonunit charges have a summable endpoint bound

The argument of \(1+te^{i\theta}\) is chosen continuously
from its positive value at \(\theta=0\).
For real \(|t|<1\), its real part stays positive.
Differentiating (17) gives
\[
 \begin{aligned}
 \sigma'(\theta)
  &=\frac{3(\theta-\pi)}{2\pi}
       -\frac1\pi\sum_\nu\arg(1+t_\nu e^{i\theta}),\\
 \sigma''(\theta)
  &=\frac1{2\pi}\sum_\nu
          \frac{1-t_\nu^2}{|1+t_\nu e^{i\theta}|^2}>0.
 \end{aligned}
 \tag{21}
\]
Thus \(\sigma'\) increases from \(-3/2\) to \(3/2\).
On a fixed real compact cube, its second derivative is bounded
above and below by positive constants, and every fixed higher
derivative is uniformly bounded.

For \(|\ell|\ge2\), set \(v_\ell=\sigma'-\ell\).
Then \(|v_\ell|\ge|\ell|-3/2\). The endpoint values of
\(a_N\) vanish, and
\[
                    a_N'(0)=a_N'(2\pi)=A_N(0).
 \tag{22}
\]
Two integrations by parts in (20) give a second boundary term
proportional to
\[
 \frac{A_N(0)e^{iN\sigma(0)}}{N^2}
       \left\{(3/2-\ell)^{-2}-(-3/2-\ell)^{-2}\right\}.
 \tag{23}
\]
Its size is \(O_\rho(N^{-2}|\ell|^{-3})\); the leading
\(|\ell|^{-2}\) terms cancel because (22) and the endpoint
phases agree.

For completeness, after the first integration the new amplitude
is \((a_N/v_\ell)'\). After the second, the remaining integral
has amplitude \(((a_N/v_\ell)'/v_\ell)'\).
One more integration bounds its boundary and integral by
\(C_\rho N^{-3}|\ell|^{-3}\), using the uniform \(C^3\)
amplitude bounds and bounded phase derivatives.
Consequently
\[
 \boxed{\qquad
              |I_{\ell,N}|
                  \le C_\rho N^{-2}|\ell|^{-3}
                          \qquad(|\ell|\ge2).
 \qquad}
 \tag{24}
\]
The source-weighted complement \(N^2\sum_{|\ell|\ge2}
|\ell I_{\ell,N}|\) is therefore \(O_\rho(1)\).
This estimate keeps the endpoint terms; it does not assume
they vanish separately.

## 5. The two unit contributions add with a nonzero coefficient

Define
\[
 h(\theta)=3\theta-2\sum_\nu\arg(1+t_\nu e^{i\theta}).
 \tag{25}
\]
It has positive derivative, \(h(0)=0\), and \(h(\pi)=3\pi\).
There is a unique \(\theta_*\in(0,\pi)\) with \(h(\theta_*)=\pi\).
It is the stationary point of \(\sigma(\theta)+\theta\).
The stationary point of \(\sigma(\theta)-\theta\) is
\(2\pi-\theta_*\). Both stay a fixed distance from the
endpoints on a compact parameter cube.

Since \(A_N\) and \(\sigma\) are reflection-even while
\(\sin\theta\) is reflection-odd,
\[
                              I_{-\ell,N}=-I_{\ell,N}
 \tag{26}
\]
exactly, with no complex conjugation. The factors \(\ell\)
in (19) therefore make the two unit contributions add.

The one-dimensional stationary-phase estimate, uniform in this
compact family, is
\[
 I_{1,N}=
 -\sin\theta_*\,A_*(\theta_*)\,
 e^{\,iN(\sigma(\theta_*)+\theta_*)+i\pi/4}
 \sqrt{\frac{2\pi}{N\sigma''(\theta_*)}}
                              +O_\rho(N^{-3/2}).
 \tag{27}
\]
The phase at \(2\pi-\theta_*\) differs by \(-2\pi\);
its exponential is unchanged because \(N\) is an integer.
The minus sign is its actual sine amplitude.

Here the standard stationary-phase calculation is elementary
and uniform: on a fixed neighborhood of the critical point use
the signed square root of twice the phase difference as coordinate.
The phase becomes \(y^2/2\), and the transformed amplitude has
uniform derivatives. Its constant term integrates to
\(e^{i\pi/4}\sqrt{2\pi/N}\), by the Gaussian integral with
positive damping removed. The odd linear term vanishes under an
even cutoff, and the quadratic remainder costs \(O(N^{-3/2})\).
For the latter bound, integrate its \(y^2\) factor once using
\(\partial_y e^{iNy^2/2}=iNy e^{iNy^2/2}\); the remaining
smooth quadratic-phase integral is \(O(N^{-1/2})\), as follows
by splitting at \(|y|=N^{-1/2}\) and integrating by parts outside.
Away from that neighborhood, two integrations by parts give
\(O(N^{-2})\), retaining the zero endpoint values of \(a_N\).
Equation (13) permits replacing \(A_N\) by \(A_*\) at the
critical point with an additional \(O(N^{-3/2})\) error.
All coordinate and cutoff bounds are uniform by (21).

Substituting (24), (26), and (27) into (18)--(19) gives
\[
 \begin{aligned}
 \mathcal C_N={}&(-1)^N i\chi_N^3 e^{i\pi/4}
       \left[\prod_\nu D_N(t_\nu)\right]
       K(\mathbf t)\,
 e^{\,iN(\sigma(\theta_*)+\theta_*)}
                                  (1+O_\rho(N^{-1})),\\
 K(\mathbf t)&=
    \frac{2\sin\theta_*\,A_*(\theta_*)}{\sqrt{h'(\theta_*)}}>0 .
 \end{aligned}
 \tag{28}
\]
The higher charges contribute \(O(N^{-3/2})\) after the
normalization in (18); the stationary error is \(O(N^{-1})\).
The positive coefficient \(K\) is bounded away from zero
on every compact real cube.

## 6. Eliminating the implicit saddle

Write \(s_1=\sum_\nu t_\nu\),
\(s_2=\sum_{\mu<\nu}t_\mu t_\nu\), \(s_3=t_1t_2t_3\),
and put \(A_0=1+s_3>0\).
At \(w=e^{i\theta_*}\), exponentiating (25) gives
\[
 \prod_\nu(w+t_\nu)+\prod_\nu(1+t_\nu w)
 =(w+1)\{A_0(w^2-w+1)+(s_1+s_2)w\}=0 .
 \tag{29}
\]
Since \(w\ne-1\),
\[
                      z_*:=2\cos\theta_*
                               =1-\frac{s_1+s_2}{1+s_3}.
 \tag{30}
\]
In particular \(z_*\in(-2,2)\) throughout the real cube.

Let \(b_\nu=1+t_\nu z_*+t_\nu^2\). Direct substitution gives
\[
 b_\nu=
  \frac{(1+t_\nu)(1-t_\nu t_\mu)(1-t_\nu t_\lambda)}
       {A_0},\qquad
 4\sin^2(\theta_*/2)=\frac{\prod_\nu(1+t_\nu)}{A_0},
 \tag{31}
\]
where \(\{\nu,\mu,\lambda\}=\{1,2,3\}\).
Differentiate the polynomial in (29) on the unit circle at its
root. Equivalently differentiate the Blaschke product in (25).
Taking absolute values gives
\[
 h'(\theta_*)\sqrt{\prod_\nu b_\nu}
                     =4A_0\cos(\theta_*/2)\sin\theta_* .
 \tag{32}
\]
Using (31)--(32) in \(K^2\) proves
\[
                        K^2=\prod_{\mu<\nu}(1-t_\mu t_\nu)^{-1}.
 \tag{33}
\]
Since \(K>0\), this is the amplitude \(B\) in (3).

The stationary action without its fixed constant is
\[
 \Psi_*=\sigma(\theta_*)+\theta_*-\frac{3\pi}{4}.
 \tag{34}
\]
Its envelope derivative is
\[
 \partial_{t_\nu}\Psi_*=
   \frac{\log b_\nu-2\log(1+t_\nu)}{2\pi t_\nu}.
 \tag{35}
\]
All arguments of these real logarithms are positive.
At \(t_\nu=0\), the quotient is interpreted by continuity.
Substituting (31) into (35) and integrating gives precisely
the dilogarithm expression in (3). Its constant is fixed at
\(\mathbf t=0\): \(\theta_*=\pi/3\) and
\(\Psi_*=-\pi/12\).

Finally the exact level-phase identity
\[
              i\chi_N^3 e^{\,3\pi iN/4}
                              =\kappa^3e^{-3\pi i/(4N)}
 \tag{36}
\]
turns (28) into (4). This completes the proof.

## 7. Scope and complete proof sources

The theorem estimates one universal joint source, not its
absolute-value envelope. Its nonzero coefficient comes from the
prescribed finite source after its zero-charge cancellation,
unit-charge addition and endpoint control.

The proof uses real phase and positivity of (21). For complex
generating parameters, endpoint terms can have a different
exponential scale. No fixed complex neighborhood, global
zero-free domain, or continuation of the asymptotic through
such a connection is proved. The estimate does not place
the generating variables of an arbitrary short-filled geometric
component in this real cube.

All repeated-root data, both original parities, the odd simple
node and the explicit scalar factors in (4) remain present.
No generic-\(q\) or peripheral family is inferred from this
fixed-root statement.

## Complete proof sources

Both complete texts were read at the matching pins. The first
supplies the exponentially accurate initialized section with
its physical Hermite data; the second fixes the entire tensor,
the original crossing jets and the precise Frobenius residue.

| Source | SHA-256 |
|---|---|
| [Full-degree generating section](research_full_degree_centered_generating_section.md) | 6fbef2085aca79503518745a08d3466ec84cd337ec8131944e2aebb9c95c2f6b |
| [Initialized finite tensor source](research_centered_tensor_finite_6phi5_source.md) | 238b5fd4daeca0293ae705d1a4c1189824129a0278e086e250207e8d51ed3f53 |

No novelty is claimed for Poisson summation, stationary phase,
or elementary Blaschke-product identities. The source-specific
content is the actual calibrated interpolation, the exact
zero-charge cancellation, the addition of the two unit
contributions, the summable endpoint bound, and their explicit
joint phase and amplitude for (2).

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
