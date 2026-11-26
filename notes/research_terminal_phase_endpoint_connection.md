# Exact endpoint connection and its full Jordan weights

Private written proof, 17 November 2026. The terminal phase grid has
an explicitly initialized polynomial connection. Its finite generating
equation retains the last-row current. The prescribed endpoint sees
every local Jordan block with explicit nonzero, polynomially sized
resolvent coefficients. This does not estimate their coherent
recombination or the selected geometric contribution after a whole word.

## 1. Actual terminal operator and finite initialization

Use the terminal coefficient-clock representation of [O]. Put
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \omega=q^\sigma,\quad \tau=\omega^2,
 \quad a=-\omega,\quad a_j=a\tau^j.
 \tag{1}
\]
For a degree-\(d\) attachment \(F(c,y)=\sum_i f_i c^iy^{d-i}\),
its phase coordinates are \(\gamma_j=\sum_i f_i a_j^i\).
The actual retained-face Casimir \(C=C_c=-T_c\) acts by
\[
 (C\gamma)_j=\alpha_j\gamma_{j+1}
                  +\delta_j\gamma_j+\beta_j\gamma_{j-1},
 \quad
 \begin{cases}
 \alpha_j=\omega(1-\tau^{-j-1}),\\
 \beta_j=\omega^{-1}(1-\tau^{-j}),\\
 \delta_j=2\omega^{-1}\tau^{-j}.
 \end{cases}
 \tag{2}
\]
The endpoints are literal: \(\beta_0=\alpha_d=0\). Every other
off-diagonal coefficient is nonzero. In particular the cyclic notation
of the phase grid does not insert a wrap arrow. Its characteristic
polynomial is
\[
 P_N(z)=\det(zI-C)
   =\prod_{s=0}^d(z-c_s)
   =2\operatorname{ChebT}_N(z/2)+2,\qquad
 c_s=\omega\tau^s+\omega^{-1}\tau^{-s}.
 \tag{3}
\]
For \(N\ge3\), these are the original operator and full Hermite
annihilator of [O]. The same polynomial Casimir formula at \(N=2\)
gives, directly,
\[
 C=\begin{pmatrix}
 2\omega^{-1}&\omega-\omega^{-1}\\
 \omega^{-1}-\omega&2\omega
 \end{pmatrix},\qquad \omega^{-1}=-\omega,\quad C^2=0,
 \tag{4}
\]
so (2)--(3), with \(P_2(z)=z^2\), hold there as well.

Define \(p_{-1}=0,p_0=1\), and, for \(0\le j<d\), define \(p_{j+1}\)
by the initialized equation
\[
 \alpha_jp_{j+1}(z)=(z-\delta_j)p_j(z)-\beta_jp_{j-1}(z).
 \tag{5}
\]
Every denominator is nonzero. Thus \(p_j\) is a degree-\(j\)
polynomial with leading coefficient
\((\alpha_0\cdots\alpha_{j-1})^{-1}\).
For \(p(z)=(p_0(z),\ldots,p_d(z))^{\mathsf T}\), the exact
remaining row is
\[
 \boxed{\ (C-zI)p(z)=-\frac{P_N(z)}{N\omega^d}e_d.\ }
 \tag{6}
\]
Indeed, if \(D_j(z)\) is the determinant of the leading \(j\)-row
minor of \(zI-C\), its continuant recurrence gives
\(D_j=(\alpha_0\cdots\alpha_{j-1})p_j\) for \(j\le d\).
The final continuant is \(P_N\). Also
\[
 \prod_{j=0}^{d-1}\alpha_j
   =\omega^d\prod_{r=1}^d(1-\tau^{-r})=N\omega^d,
 \tag{7}
\]
which proves the constant and sign in (6).

The normalization is an actual row identity, not an eigenvector
choice made after a scalar evaluation:
\[
                  e_j^{\mathsf T}=e_0^{\mathsf T}p_j(C).
 \tag{8}
\]
It follows by induction from the tridiagonal rows in (2).
For example
\[
 p_1(z)=\frac{z-2\omega^{-1}}{\omega-\omega^{-1}}.
 \tag{9}
\]
For fixed \(z\ne2\), this initial ratio has order \(N\).
That fact does not identify a whole-word geometric solution with
an exact eigenvector of this one finite Casimir.

## 2. The generating equation keeps the endpoint current

Let \(G_N(t,z)=\sum_{j=0}^d p_j(z)t^j\). Multiplying (5) by
\(\omega\tau^j\) gives
\[
 (1-\tau^{j+1})p_{j+1}
      =(2-\omega\tau^jz)p_j-(1-\tau^j)p_{j-1}.
 \tag{10}
\]
Summing this recurrence, with its finite endpoint (6), proves the
polynomial identity
\[
 \boxed{\ (1-t)^2G_N(t,z)
 -(1-\omega zt+\tau t^2)G_N(\tau t,z)
                =-\frac{P_N(z)}N\,t^N.\ }
 \tag{11}
\]
The coefficients below \(t^N\) vanish by (10). Its \(t^N\)
coefficient is \(-P_N(z)/N\) by (6) and \(\omega^N=-1\);
the \(t^{N+1}\) coefficient is zero because \(\tau^N=1\).
No periodic homogeneous extension replaces this last equation.

There is an explicit finite exponential solution. Write
\(\mathcal C_r(z)=2\operatorname{ChebT}_r(z/2)\). In
\(\mathbb C[z,t]/(t^N)\),
\[
 G_N(t,z)=
 \exp\left\{\sum_{r=1}^d
       \frac{2-\omega^r\mathcal C_r(z)}
            {r(1-\tau^r)}\,t^r\right\}\pmod{t^N}.
 \tag{12}
\]
The exponential and logarithm are finite operations in this ring;
all displayed denominators are nonzero. To verify (12), factor
\(1-\omega zt+\tau t^2=(1-\omega vt)(1-\omega v^{-1}t)\),
where \(z=v+v^{-1}\). Taking the formal logarithm of (11)
modulo \(t^N\) gives its coefficient formula. The result is
polynomial in \(z\) and independent of the choice of \(v\).

At every physical root the answer is a finite product. For
\((u;\tau)_k=\prod_{r=0}^{k-1}(1-u\tau^r)\),
\[
 \boxed{\ G_N(t,c_s)
  =(\tau^{s+1}t;\tau)_{d-s}(\tau^{-s}t;\tau)_s,\quad 0\le s\le d.\ }
 \tag{13}
\]
In fact (12) first gives the formal ratio
\((\tau^{-s}t;\tau)_s/(t;\tau)_{s+1}\) modulo \(t^N\).
Multiplication by \(1-t^N\) preserves these coefficients and
cancels its denominator, giving exactly the degree-\(d\) product
(13). The factor \(1-t^N\) is essential; the bare rational
function is not equal to \(G_N\).

The top coefficient is particularly simple:
\[
                         p_d(c_s)=\tau^{-s(s+1)}.
 \tag{14}
\]
The sum of the product exponents in (13) is
\(Nd/2+Ns-s(s+1)\), and
\((-1)^d\tau^{Nd/2}=1\), proving (14).
The paired labels \(s,d-s\) give the same physical polynomial.

At a double root, the same generating function also determines the
top spectral derivative:
\[
 \frac{p_d'(c_s)}{p_d(c_s)}
       =\frac{d-2s}{\lambda_s-\lambda_s^{-1}},
 \qquad \lambda_s=\omega\tau^s,\quad s<d-s.
 \tag{14a}
\]
To prove it, differentiate (12) at \(c_s=\lambda_s+\lambda_s^{-1}\).
The finite geometric sum in its logarithmic derivative gives
\[
 p_d'(c_s)=\frac1{\lambda_s-\lambda_s^{-1}}
   \sum_{k=-s}^s[t^d]\,
             G_N(t,c_s)\frac{\tau^kt}{1-\tau^kt}.
 \tag{14b}
\]
The indicated coefficient equals
\(\tau^{kd}G_N(\tau^{-k},c_s)-p_d(c_s)\).
For \(-s\le k<0\), the evaluation is zero by (13).
For the remaining terms write
\[
 \frac{(\tau^{-s}t;\tau)_s}{(t;\tau)_{s+1}}
       =\sum_{k=0}^s\frac{b_k}{1-\tau^kt}.
 \tag{14c}
\]
Its poles are distinct, and the numerator and denominator have
no common factor because \(s<d-s\). Multiplication by \(1-t^N\)
gives \(G_N(\tau^{-k},c_s)=Nb_k\). At infinity (14c) equals
\(-p_d(c_s)/t+O(t^{-2})\), hence
\(\sum_{k=0}^sb_k\tau^{-k}=p_d(c_s)\).
Since \(\tau^{kd}=\tau^{-k}\), the evaluations in (14b) sum to
\(Np_d(c_s)\); subtracting its \(2s+1\) copies of \(p_d\)
proves (14a). No derivative of a root-only product with a
discretely varying label \(s\) was used.

## 3. Every full local Jordan block is initialized

The distinct double roots are represented by \(s<d-s\).
When \(N\) is odd there is also the simple root
\(s=d/2,\ c_s=-2\). Differentiating (6) at a double root gives
\[
 (C-c_sI)p(c_s)=0,\qquad
 (C-c_sI)p'(c_s)=p(c_s),\qquad
 p_0(c_s)=1,\quad p'_0(c_s)=0.
 \tag{15}
\]
The columns \(p(c_s),p'(c_s)\) at double roots, and \(p(-2)\)
at the odd simple root, form a basis. Indeed their matrix is
the usual confluent evaluation matrix of a polynomial basis
of degrees \(0,\ldots,d\), with nonzero leading coefficients.
Confluent evaluation at the roots of the monic degree-\(N\)
polynomial \(P_N\) is invertible.

Consequently, for every function \(f\) defined by its full
Hermite data modulo \(P_N\),
\[
 f(C)p(c)=f(c)p(c),\qquad
 f(C)p'(c)=f(c)p'(c)+f'(c)p(c).
 \tag{16}
\]
In particular this retains the original derivative of every
signed crossing power. If \(r_N\) is the original normalized
crossing unit, then \(f=\kappa^p r_N^p\), \(p\in\mathbb Z\),
has \(f'(c)=\kappa^p p\,r_N(c)^{p-1}r_N'(c)\).
This is a fixed-root spectral derivative, not a genuine-\(q\)
normal or a changed meridian family.

## 4. All endpoint resolvent coefficients

Write
\[
 e_0^{\mathsf T}(zI-C)^{-1}e_0=\frac{Q_N(z)}{P_N(z)},
 \tag{17}
\]
where \(Q_N\) is the trailing \((N-1)\)-row principal minor.
No spectral root cancels from this ratio. More precisely,
\[
 \boxed{\ Q_N(c_s)=N\omega^{-d}\tau^{s(s+1)}.\ }
 \tag{18}
\]
Here is a proof keeping the bilinear convention. The diagonal
matrix \(W=\operatorname{diag}(1,\tau,\ldots,\tau^d)\) satisfies
\(C^{\mathsf T}W=WC\), since
\(\alpha_j/\beta_{j+1}=\tau\). At a root, (15) and the basis
argument show that \(zI-C\) has rank \(N-1\). Its adjugate is
therefore a nonzero multiple of \(p(c_s)p(c_s)^{\mathsf T}W\).
Its \((0,d)\) entry is the continuant cofactor
\(\prod_{j<d}\alpha_j=N\omega^d\). Since \(p_0=1\), its
\((0,0)\) entry is
\[
 \frac{N\omega^d}{\tau^d p_d(c_s)}
       =N\omega^{-d}\tau^{s(s+1)},
 \tag{19}
\]
as asserted. This is a transpose identity, not a positivity claim.

The cofactor derivative has an equally exact normalization. Let
\(R_{\rm int}(z)\) be the determinant of the central \(N-2\) rows
and columns of \(zI-C\), with the empty determinant equal to one.
The tridiagonal determinant identity is
\[
 D_d(z)Q_N(z)-P_N(z)R_{\rm int}(z)
       =\left(\prod_{j<d}\alpha_j\right)
          \left(\prod_{j=1}^d\beta_j\right)=N^2.
 \tag{19a}
\]
For example, when the central block is invertible, take its
two-by-two Schur complement: the difference on the left is the
product of its two effective off-diagonal entries times the
squared central determinant. Successive elimination along the
tridiagonal chain gives the displayed two products. Polynomial
continuation proves the identity without the invertibility
assumption. Substituting \(D_d=N\omega^d p_d\) gives
\[
 Q_Np_d=N\omega^{-d}
            +\frac{P_N R_{\rm int}}{N\omega^d},
 \qquad
 \frac{Q_N'(c_s)}{Q_N(c_s)}
                 =-\frac{p_d'(c_s)}{p_d(c_s)}
 \tag{19b}
\]
at every double root. Thus no unknown cofactor derivative remains.

At a double root,
\[
 P_N(c_s+\zeta)
   =\frac{N^2}{4-c_s^2}\zeta^2+O(\zeta^3).
 \tag{20}
\]
This follows by expanding
\(P_N(2\cos\theta)=2\cos(N\theta)+2\) at
\(\theta=(2s+1)\pi/N\). Hence the highest double-pole coefficient
in (17) is exactly
\[
 \boxed{\ W_{2,s}
      =\omega^{-d}\tau^{s(s+1)}
                      \frac{4-c_s^2}{N},\qquad
       \frac{16}{N^3}\le |W_{2,s}|\le\frac4N.\ }
 \tag{21}
\]
The lower bound uses
\(\sin((2s+1)\pi/N)\ge\sin(\pi/N)\ge2/N\) on these
representatives. Put \(\theta_s=(2s+1)\pi/N\) and
\(u_s=\omega^{-d}\tau^{s(s+1)}\). The accompanying simple-pole
coefficient at the same double root is
\[
 \boxed{\ W_{1,s}
   =u_s\left\{
       \frac{2i\sigma(d-2s)\sin\theta_s}{N}-\frac{c_s}{N}
          \right\},\qquad
          \frac1N\le |W_{1,s}|\le2+\frac2N.\ }
 \tag{21a}
\]
Indeed, the Chebyshev differential equation gives
\(P_N'''(c_s)/(3P_N''(c_s))=c_s/(4-c_s^2)\).
Expanding \(Q_N/P_N\) and using (14a),(19b) therefore gives
\[
 W_{1,s}=W_{2,s}
       \left\{-\frac{d-2s}{\lambda_s-\lambda_s^{-1}}
                          -\frac{c_s}{4-c_s^2}\right\},
 \tag{21b}
\]
which is (21a). Its upper bound follows directly. For the lower
bound, the two terms in braces in (21a) are respectively imaginary
and real, and
\[
 |W_{1,s}|^2=\frac{4\cos^2\theta_s}{N^2}
             +4(1-\theta_s/\pi)^2\sin^2\theta_s.
 \tag{21c}
\]
If \(|\cos\theta_s|\ge1/2\), the first term suffices.
Otherwise \(\theta_s\in(\pi/3,2\pi/3)\), so the second term
gives \(|W_{1,s}|\ge1/\sqrt3\ge1/N\).

For the odd simple root, \(P_N'(-2)=N^2\),
so its residue is
\[
 \boxed{\ W_{\rm simple}
       =\frac{\omega^{-d}\tau^{s(s+1)}}N,\qquad
                      |W_{\rm simple}|=\frac1N.\ }
 \tag{22}
\]
These statements include \(N=2\), where (4) gives the same
double-pole coefficient directly.

Thus the full initialized endpoint functional is
\[
 e_0^{\mathsf T}f(C)e_0
  =\sum_{s<d-s}\{W_{1,s}f(c_s)+W_{2,s}f'(c_s)\}
      +\begin{cases}
          W_{\rm simple}f(-2),&N\ {\rm odd},\\
          0,&N\ {\rm even}.
        \end{cases}
 \tag{22a}
\]
This follows by residues, or polynomial Hermite calculus, and
holds for every function of the full finite Casimir algebra.
Although all its displayed weights have polynomial upper and
lower bounds, their signed sum can cancel. Alternating the two
retained faces also changes the initialized bases; no bound for
those whole-word connections or for a selected geometric branch
is inferred.

## 5. The literal cap-prepared return amplitude

The signed original corner in [C], with its scalar retained, is
\[
 B_\sigma(c,y)
    =\kappa^\sigma\sum_{i=0}^d
                   a^{d-i}c^iy^{d-i},\qquad
 \kappa=q^{d^2/2}.
 \tag{23}
\]
Its entire phase vector is exactly
\[
 \gamma_j(B_\sigma)
       =N\kappa^\sigma a^d\delta_{j0},\qquad
                      \kappa^{2\sigma}a^d=1.
 \tag{24}
\]
This is the finite geometric sum of \(\tau^{ji}\). Therefore
for any literal word \(U\) in the two retained-face operators
allowed by [O], including their full signed crossing scalars,
\[
 \boxed{\ \kappa^\sigma\ell_a(U B_\sigma)
                            =N(U_{\rm phase})_{00}.\ }
 \tag{25}
\]
Equation (25) applies to this actual cap-prepared attachment and
the specified operator placements. It does not rewrite every
original graph as such a word. An arbitrary completed attachment
retains its own full phase vector and the prescribed row
\(\kappa^\sigma\gamma_0\).

## Complete direct sources and coverage

Both complete direct texts and their used implications were read.
The complete research_rational_word_local_source_system.md was
also read for coverage: its arbitrary-word forced system already
retains finite initialization, all inputs, turns and endpoint
currents. The new information here is the explicit terminal
connection (11)--(14c) and the explicit full local
resolvent weights (18)--(22a), not a claim that finite initialization
was previously missing. No mathematical programs or numerical
evaluations were used.

| Label | Source | SHA-256 |
|---|---|---|
| O | [Root-orbit retained-face operators](research_root_orbit_cap_observable_operators.md) | 68b1e668bd6af388dc22bfc23652ae6f5d2ea09b5ecc036b8be4a3c299451893 |
| C | [Literal cap-turn interface](research_trace_one_mark_and_cap_turn_interface.md) | d1be51d8fcaad2dd4886769ed5e172ceeaff66891c5cb1e46f29917d5ee97e48 |
