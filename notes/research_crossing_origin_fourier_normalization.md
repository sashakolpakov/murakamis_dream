# Fourier selection of the actual zero-activity crossing source

Written research proof, 22 November 2026.

The original scalar with two zero coherent activities has its canonical
Gamma normalization on every compact subset of its positive-action locus.
The proof starts from its own full two-variable grid. It does not take
an unproved uniform limit of the three-variable unit-activity theorem.
The resulting normalization is nonzero, with its original complex phase.

## 1. The source and the canonical comparison

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 p=Q^{-1},\quad \eta=(-1)^d,\quad \kappa=q^{d^2/2}.
 \tag{1}
\]
Use the complete centered basis of [P], with
\(\phi(f_i f_j)=\delta_{ij}\) and \(U_t=\sum_{j=0}^d t^jf_j\).
Define the actual scalar and its comparison section by
\[
 \begin{split}
 \Psi_N(H,K)&=\phi(f_0^2U_{-H}U_{-K})
               =\Phi_N(0,H,K),\\
 \Theta_N(h,k)&=\frac{\kappa^2}{N^2}
 \frac{\mathfrak F_N(N(1-h)-1/2)^2
       \mathfrak F_N(N(1-k)-1/2)^2}
      {\mathfrak F_N(N(1-h-k))},\\
 H&=e^{-2\pi ih},\qquad K=e^{-2\pi ik}.
 \end{split}
 \tag{2}
\]
The factorial and all its marks are those of [E,G]. The source is
separately polynomial of degree at most \(d\). This is activity zero
in the first argument, hence two factors \(f_0\); it is not the
unit-activity readout \(\Phi_N(q^{-1},H,K)\).

Put
\[
 J(t)=\int_0^t\log|2\sin\pi u|\,du,\qquad
 V(h,k)=J(h+k)-2J(h)-2J(k),\qquad
 \Omega=\{h,k>0:\ h+k<1,\ V(h,k)>0\}.
 \tag{3}
\]

**Theorem 1.** For every compact \(\mathcal K\subset\Omega\),
there are a fixed complex neighborhood \(\mathcal U\) of
\(\mathcal K\) and \(\delta>0\) such that
\[
 \boxed{\quad
 \Psi_N(e^{-2\pi ih},e^{-2\pi ik})/\Theta_N(h,k)
       =1+O(e^{-\delta N})\quad\hbox{on }\mathcal U .
 \quad}
 \tag{4}
\]
On a smaller fixed neighborhood every fixed-order derivative of
the ratio minus one is also \(O(e^{-\delta N})\), after decreasing
\(\delta\) if needed. The statements include every sufficiently
large integer level, both parities and composite levels.
In particular the original scalar is nonzero there and
\[
               \log|\Psi_N|=NV(h,k)+O(\log N)
                         \quad\hbox{on real }\mathcal K.
 \tag{5}
\]
The proof below also fixes the full leading phase and amplitude.

## 2. The complete grid and its global magnitude profile

Set \(a_j=(j+1/2)/N\), \(H_j=q^{-1}Q^{-j}\), \(0\le j\le d\).
The full three-variable grid of [P] implies
\[
 \Psi_N(H_j,H_\ell)=
 \frac{\kappa^2}{N^2}
       \frac{F_{d-j}^2F_{d-\ell}^2}{F_{d-j-\ell}}
       \quad(j+\ell\le d),
 \qquad \Psi_N(H_j,H_\ell)=0\quad(j+\ell>d),
 \tag{6}
\]
where \(F_r=(Q;Q)_r\) only at \(0\le r<N\).
Here is a direct justification of taking activity zero.
At these two fixed grid arguments, the canonical three-variable
section of [G] is, when \(j+\ell\le d\), the right side of (6)
times
\[
  \prod_{r=0}^{j-1}(1-Cq^{-1}Q^{-r})
  \prod_{s=0}^{\ell-1}(1-Cq^{-1}Q^{-s}).
 \tag{7}
\]
This follows from its exact factorial shifts. It is a polynomial
of degree \(j+\ell\le d\), equal to the original source at all
\(N\) remaining grid points by [P]. Thus they are identical
polynomials in \(C\); evaluation at zero proves (6).
Outside this support the original Newton product \(e_je_\ell\)
vanishes in the whole algebra. The fixed pair factorial in the
canonical denominator has its pole at \(d-j-\ell\); its
meromorphic restriction is zero as well. No division by a
vanishing root factorial is used.

Consequently \(\Theta_N(a_j,a_\ell)\) is exactly (6).
If \(S_r=\prod_{t=1}^r2\sin(\pi t/N)\), reflection
\(S_rS_{d-r}=N\) gives on support
\[
                  |\Psi_N(H_j,H_\ell)|
                       =N\,\frac{S_{j+\ell}}{S_j^2S_\ell^2}.
 \tag{8}
\]
The uniform endpoint estimates proved in [F, Section 2] are
\[
 \log S_r=NJ(r/N)+O(\log N),\qquad
 |J(x+t)-J(x)|\le C|t|\log(e/|t|).
 \tag{9}
\]
They yield uniformly on the entire supported grid
\[
       \log|\Psi_N(H_j,H_\ell)|
             =NV(a_j,a_\ell)+O(\log N).
 \tag{10}
\]
All support faces, including \(a_j+a_\ell=1\), are included.
Unsupported data are exactly zero.

The continuous profile has the unique global maximum on
\(\overline{\mathcal T}=\{h,k\ge0:h+k\le1\}\) at
\[
                 z_*=(1/4,1/4),\qquad M=-4J(1/4)>0 .
 \tag{11}
\]
Indeed \(J(1-t)=-J(t)\), and its minimum is \(J(1/6)<0\);
put \(A=-J(1/6)>0\). On \(h=0\) or \(k=0\), the boundary
maximum of \(V\) is at most \(A\), and on \(h+k=1\) its value
is zero. On the other hand,
\[
 V(1/6,1/6)=
 [J(1/3)-2J(1/6)]+2A>A.
 \]
The bracket is positive by the strict fixed-sum concavity of
\(J(a+b)-J(a)-J(b)\), proved in [F].
Every maximum is therefore interior. Its critical equations are
\[
 2\sin\pi(h+k)=(2\sin\pi h)^2=(2\sin\pi k)^2.
 \]
In the open triangle they force \(h=k=1/4\).
At that point \(D^2V=-2\pi I\). This proves (11), and compactness
gives a strict gap away from every neighborhood of \(z_*\).
No global concavity of \(V\) is assumed.

## 3. The canonical phase is strictly inside the Fourier band

The shifted strip expansion in [E,G], or [F, equation (17)], gives
on fixed complex compact sets with
\(0<\Re h,\Re k,\Re(h+k)<1\)
\[
 \Theta_N=\kappa^2N^{-1/2}b(h,k)e^{NS_0(h,k)}
                                      (1+O(N^{-1})),
 \tag{12}
\]
\[
 \begin{split}
 S_0&=\frac{3\operatorname{Li}_2(1)
       -2\operatorname{Li}_2(H)-2\operatorname{Li}_2(K)
       +\operatorname{Li}_2(HK)}{2\pi i},\\
 b(h,k)&=-\mathfrak h(1-h-k)^{-1},\qquad
                  \mathfrak h(w)^2=i(1-e^{2\pi iw}).
 \end{split}
 \tag{13}
\]
All branches are canonical. Each squared numerator factorial,
including its shift \(-1/2\), contributes \(iN\); the denominator
contributes \(\sqrt N\,\mathfrak h(1-h-k)\). This proves the
minus sign and the power of \(N\).
On the real triangle the dilogarithm boundary values give
\[
 S_0=V-\frac{\pi i}{2}[h+k-(h-k)^2].
 \tag{14}
\]
At \(z_*\), each derivative
\(\partial_{\Im h}\Re S_0,\partial_{\Im k}\Re S_0\)
equals \(\pi/2\). Choose a small fixed complex product box and
\(\alpha>0\) such that throughout that box, jointly in both variables,
\[
 \alpha\le\partial_{\Im h}\Re S_0\le2\pi-\alpha,\qquad
 \alpha\le\partial_{\Im k}\Re S_0\le2\pi-\alpha .
 \tag{15}
\]
The canonical section is holomorphic and nonzero there.

## 4. A two-variable cardinal contour selects the actual normalization

Choose a small real box about \(z_*\). For each \(N\), choose each
pair of angular endpoints in \(N^{-1}\mathbb Z\), within \(O(N^{-1})\)
of that box's endpoints, and choose a small fixed contour height
\(\tau>0\). The resulting product rectangles lie in the box of (15).
Let \(I_N\) contain the half-grid nodes in each real interval.
Write \(D_N(z)=1+z^N\) and
\[
 \ell_j(t)=\frac1N\sum_{a=0}^d(t/H_j)^a,\qquad
 P_i f=\sum_{j\in I_N}f(H_j)\ell_j,\qquad R_i=I-P_i .
 \]
The positively oriented activity-sector contour \(\mathcal C_N\)
has the exact residue formula
\[
 R_i f(t)=\frac{D_N(t)}{2\pi i}
       \int_{\mathcal C_N}\frac{f(z)}{(z-t)D_N(z)}\,dz .
 \tag{16}
\]
It follows by residues at \(z=t,H_j\); at a node target use
continuity. The local angular logarithm is used for \(\Theta_N\).

By (11) there is \(\gamma>0\) such that every real face of the
larger box, and every supported grid point outside its interior,
has \(V\le M-\gamma\). On a vertical contour side its endpoint
choice gives \(|D_N(z)|=1+e^{2\pi Ny}\). On a horizontal side,
\(|D_N(z)|\ge\tfrac12 e^{2\pi N\max(y,0)}\) for large \(N\).
Integrating (15) in the imaginary direction and using (12) gives
\[
 \frac{|\Theta_N(x+iy,\cdot)|}{|D_N(z)|}
      \le N^B e^{N[V(x,\cdot)-\alpha|y|]} .
 \tag{17}
\]
For real targets in a smaller box, the Cauchy denominators in (16)
stay uniformly separated from zero and \(|D_N(t)|\le2\).
With \(\delta_0=\min(\gamma,\alpha\tau)>0\), it follows that
\(|R_i\Theta_N|\le N^Be^{N(M-\delta_0)}\), uniformly with the
other real coordinate anywhere in the larger box.
Since \(|\ell_j(t)|\le1\) on the real angular circle, the identity
\(I-P_1P_2=R_1+P_1R_2\) gives the same bound, with polynomial
cost, for the local two-variable interpolation error.

The full original interpolant of the data (6) differs from
\(P_1P_2\Theta_N\) only by its nodes outside \(I_N^2\).
Equation (10) bounds that entire discarded sum by
\(N^Be^{N(M-\gamma)}\). Thus the discarded data are controlled
before a conclusion about the scalar is drawn.

For precision the same contours give a fixed complex seed.
If target heights have modulus at most \(t_0\), then
\[
 |\ell_j(t)|\le e^{2\pi N(\Im a)_+},\qquad
 |D_N(t)|\le2e^{2\pi N(\Im a)_+}.
 \]
The discarded grid sum costs at most \(e^{4\pi Nt_0}\).
For the local remainder expand
\[
                 I-P_1P_2=R_1+R_2-R_1R_2.
 \]
Each term is an iterated integral (16). Replace unintegrated
target imaginary parts by zero, at cost at most \(e^{4\pi Nt_0}\).
Move integrated imaginary parts to their contour values one at
a time. The joint bound (15) gives (17) in each coordinate.
Each nonempty contour term retains either a real-face gap
\(\gamma\) or a horizontal loss \(\alpha\tau\).
The numerator factors \(D_N(t)\) cost at most another
\(e^{4\pi Nt_0}\). Hence the complete absolute error is at most
\[
                    N^B e^{N(M-\delta_0+8\pi t_0)} .
 \tag{18}
\]
Choose \(8\pi t_0<\delta_0/4\). Shrink the real target box and
then its imaginary height so that \(\Re S_0>M-\delta_0/4\).
The nonzero amplitude in (12) turns (18) into (4) on a fixed
complex neighborhood of \(z_*\), including all fractional classes.

## 5. Balancing paths and exact sourced transport

The unbalanced identity of [F], set at activity \(C=0\), gives
\[
 (1-H/q)^2\Psi_N(pH,K)-(1-HK)\Psi_N(H,K)
       =Hj_0,\qquad j_0=\frac{\eta}{N}(2+H^N+K^N).
 \tag{19}
\]
There is the corresponding equation in \(K\).
Exact factorial shifts in (2) give
\[
       \Theta_N(h+1/N,k)
          =\frac{1-HK}{(1-H/q)^2}\Theta_N(h,k).
 \tag{20}
\]
For \(E_N=\Psi_N/\Theta_N-1\), therefore,
\[
 E_N(h+1/N,k)-E_N(h,k)
       =\frac{Hj_0}{(1-H/q)^2\Theta_N(h+1/N,k)} .
 \tag{21}
\]

The locus \(\Omega\) contains \((0,1/2)^2\), because there
\[
 V(h,k)=[J(h+k)-J(h)-J(k)]-J(h)-J(k)>0,
 \tag{22}
\]
because the bracket is positive and \(J(t)<0\) for \(0<t<1/2\).
Every point of \(\Omega\) has a path to \(z_*\) along which \(V\)
does not decrease. First fix \(R=h+k\) and balance its two
coordinates to \((R/2,R/2)\). The fixed-sum second derivative is
\[
 \frac{d^2}{dt^2}V(t,R-t)
       =-\frac{2\pi\sin\pi R}{\sin\pi t\sin\pi(R-t)}<0 .
 \tag{23}
\]
Symmetry makes the balanced point its unique maximum.
Next move on the diagonal from \(t=R/2\) to \(t=1/4\).
For \(W(t)=V(t,t)\) one has \(W'(t)=2\log\cot(\pi t)\),
which has the sign toward its maximum at \(1/4\).
Both segments therefore remain in \(\Omega\) with
\(V\ge V(h,k)\).

For a compact \(\mathcal K\subset\Omega\), the union of these
two-segment paths is compact in the open triangle and has
\(V\ge v_0:=\min_{\mathcal K}V>0\).
Choose a fixed closed tube \(\mathcal L\Subset\Omega\) about that
union, with \(m_0:=\min_{\mathcal L}V\ge v_0/2\) and a buffer.
These are the domains used for propagation.

The coordinate mesh need not lie on the balanced segments.
On the coset \(a+N^{-1}\mathbb Z^2\), round their middle point
and \(z_*\) coordinatewise to \(b_N,z_N\), within \(1/(2N)\).
Digitize each segment \([a,b_N]\), \([b_N,z_N]\) by following
its successive grid-line crossings. An axis staircase so obtained
stays within \(1/N\) of that segment. Thus it stays within
\(3/(2N)\) of the original path, and has at most
\[
       N\bigl(|h-k|+|h+k-1/2|\bigr)+3<3N/2+3
 \tag{24}
\]
steps. For large \(N\) it lies in \(\mathcal L\). Its endpoint
\(z_N\) is in the established normalization box and has exactly
the target's fractional classes. Reverse it to propagate from
that seed to the target. This construction applies to all targets
uniformly on \(\mathcal K\).

For complex targets give this same real path the target's fixed
imaginary vector, with heights bounded by a sufficiently small
fixed \(t>0\). Include its seed in the complex seed box. Choose
the height so that throughout the path box
\[
                  \Re S_0\ge m_0/2,\qquad 2\pi t<m_0/4.
 \tag{25}
\]
The single-angle margins bound \(|1-H/q|\) and \(|1-K/q|\)
uniformly away from zero. Equation (12) bounds the shifted
\(\Theta_N\) below by \(N^{-B}e^{Nm_0/2}\).
Moreover \(|j_0|\le(4/N)e^{2\pi Nt}\).
Thus every normalized increment in (21) or its permutation has
modulus at most \(N^Be^{-Nm_0/4}\).
Backward steps use the negative forward increment at their lower
endpoint, with both endpoints in the same buffered path box.
Summing fewer than \(2N\) increments and the exponential seed error
proves (4). No cyclic norm or forcing value is divided by.

Enlarge \(\mathcal K\) slightly within \(\Omega\) before this
construction and then shrink the fixed complex neighborhood.
Cauchy's formula proves the derivative assertion. Combining (4)
with (12) fixes the original full leading phase and amplitude,
and proves (5). All Fourier nodes and full algebra identities
used here are valid at even and composite levels.

## Proof sources and scope

All four complete proof sources were read at matching renewed pins:

| Label | Complete source | SHA-256 |
|---|---|---|
| F | [Fourier normalization, 603 lines](research_crossing_fourier_normalization.md) | 78dd1583385974cb0d63134608a70866ca16267d179f7339eff6bd808b399f69 |
| P | [Full pairwise source, 668 lines](research_exact_pairwise_conway_source.md) | 470c9df0384274623a1aa0b6939067021894f2fea41595dfa7440081ca77f1d1 |
| G | [Canonical Gamma section, 632 lines](research_crossing_exact_gamma_source_extension.md) | f19221b384ae9c2de47beee8460df4eee30f3419df6cf0478c18569b3f464495 |
| E | [Canonical factorial, 226 lines](exact_factorial_interpolation_and_complex_contours.md) | 1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72 |

The residue-selection method is the one proved in [F]; its
two-variable source, global maximum, canonical phase and complete
source bounds have been checked here independently. Its
three-variable conclusion is not applied at activity zero.
The original cap estimate with only one factor \(f_0\) is different;
it was already covered by the single-leg radial source theorem.

This proves the normalization of \(\Phi_0\) appearing in the
origin-jet adapter on the stated parameter chamber. It does not
bound the remaining observer polynomials or their cut connectors
relative to a general original closing. No physical boundary
dimension is removed, and no filled-knot volume rate, additional
filling class, or finite-exception theorem is inferred.

Only written mathematics and text/hash inspection were used. No
mathematical program, numerical experiment, test, build, git action,
or earlier-final file edit was performed.
