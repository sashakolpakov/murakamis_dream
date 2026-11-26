# Physical moments of the second period and the adjacent interface

Research deduction, 7 November 2026. At every physical input pair,
the complete second homogeneous period is an explicit cyclotomic
matrix plus one transcendental constant times the complete homogeneous
node matrix. The original nonzero Casoratian then proves that all these
second-period values are nonzero and that its neighboring-node
annihilator is not an algebraic two-node closing row.

The same calculation gives a concrete representation of adjacent
power-two components in terms of the two periods. It does not infer
noncancellation for a prescribed knot closure or a geometric lower
bound from the period packet. No numerical evaluation is used.

## 1. Exact moments on every physical pair

Fix \(N\ge3\), and retain
\[
 D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
 P_j=(r;r)_j,\quad p_j(U)=(rU;r)_j,\quad
 \kappa=q^{D^2/2}.
 \tag{1}
\]
All algebraic coefficients below belong to the cyclotomic field
\[
                  K_N=\mathbb Q(e^{\pi i/(2N)}).
 \tag{2}
\]
It contains \(i,q,\kappa\) and all the nonzero \(P_j\), \(j<N\).
Let \(H_N\) be the complete homogeneous remainder and let
\(Z_N=\mathcal I_{2,N}\) denote the second homogeneous period in
[the homogeneous-period theorem](research_mixed_three_fourier_conditional_homogeneous_period.md).
This \(Z_N\) is not the original Fourier cap.
The same-current extension in
[full-node composition](research_mixed_three_homogeneous_period_full_node_composition.md)
and Section 3 of the period theorem puts both functions on
\[
 \mathcal S_N^2,\qquad
             \mathcal S_N=\{-1/(2N)<\Re z<1\}.
 \tag{3}
\]
In particular every physical pair \((b/N,c/N)\), \(0\le b,c<N\),
is in their exact domain.

Set \(U=e^{-2\pi is}\). The original factorial recurrences give,
on the actual midpoint line \(s=-1/(2N)+iv\),
\[
 T_N(s;b/N,c/N)
      =L_{bc}(U):=\frac{U^{-b}p_b(U)p_c(U)}{P_bP_c}
      =\sum_{j=-b}^{c}\ell^{bc}_jU^j,\qquad
                         \ell^{bc}_j\in K_N.
 \tag{4}
\]
This is an exact continuation identity, not just equality at the
summation nodes \(s=k/N\). All its exponents satisfy \(|j|<N\).

**Lemma 1.** With upward orientation and
\(k_{2,N}(s)=e^{-2\pi iNs}/(1-e^{-2\pi iNs})^2\), the moments are
\[
 \int_{-1/(2N)-i\infty}^{-1/(2N)+i\infty}
                   k_{2,N}(s)e^{-2\pi ijs}\,ds
   =
   \begin{cases}
     \displaystyle\frac1{2\pi iN},&j=0,\\[2mm]
     \displaystyle\frac{j}{N^2(1-r^j)},&0<|j|<N.
   \end{cases}
 \tag{5}
\]

*Proof.* Put \(T=e^{2\pi Nv}>0\). On this line,
\[
 U=e^{\pi i/N}T^{1/N},\qquad
 k_{2,N}(s)\,ds=\frac1{2\pi iN}\frac{dT}{(1+T)^2}.
 \tag{6}
\]
For \(|j|<N\), the resulting beta integral is absolutely convergent:
\[
 \frac{e^{\pi ij/N}}{2\pi iN}
   \int_0^\infty\frac{T^{j/N}}{(1+T)^2}\,dT
 =\frac{e^{\pi ij/N}}{2\pi iN}
       \Gamma(1+j/N)\Gamma(1-j/N).
 \tag{7}
\]
For \(j\ne0\), reflection gives
\(\Gamma(1+j/N)\Gamma(1-j/N)
 =(\pi j/N)/\sin(\pi j/N)\).
Using \(1-r^j=2i e^{-\pi ij/N}\sin(\pi j/N)\)
proves (5). For \(j=0\) the integral is one.
This argument includes negative \(j\) and both level parities.
\(\square\)

Let
\[
 \mathbf H_{bc}=H_N(b/N,c/N)=C_{0,N}(r^b,r^c),\qquad
 \mathbf Z_{bc}=Z_N(b/N,c/N),\qquad
                  \theta_N=\frac1{2\pi iN^2}.
 \tag{8}
\]
The literal finite sum of the row (4) is its root-of-unity average:
\[
 \mathbf H_{bc}=\sum_{k=0}^{N-1}L_{bc}(r^k)
                         =N\ell^{bc}_0.
 \tag{9}
\]
Only the constant mode survives, because the entire band in (4)
lies strictly between \(-N\) and \(N\).
Integrating the finite expansion (4) with (5) gives the exact matrix
decomposition
\[
 \boxed{\quad
       \mathbf Z=\theta_N\mathbf H+\mathbf R,\qquad
       \mathbf R_{bc}
          =\frac1{N^2}\sum_{\substack{-b\le j\le c\\j\ne0}}
                    \frac{j\,\ell^{bc}_j}{1-r^j}\in K_N .
 \quad}
 \tag{10}
\]
All denominators in (10) are nonzero. Thus no limiting prescription
at a physical zero is used.

There is also a direct finite derivative formula for the algebraic
part:
\[
 \boxed{\quad
 \mathbf R_{bc}=
     \frac1{N^3}\sum_{k=0}^{N-1}(N-1-k)
       \left[U\frac{d}{dU}L_{bc}(U)\right]_{U=r^k}.
 \quad}
 \tag{11}
\]
Indeed for \(j\ne0\), \(|j|<N\),
\[
       \sum_{k=0}^{N-1}(N-1-k)r^{kj}
                                  =\frac N{1-r^j}.
 \tag{12}
\]
The derivative in (11) kills the constant mode. Formula (12)
follows by differentiating the finite geometric sum before
specializing \(r^{Nj}=1\).
Equation (11) retains the normal information of this private row.
It is not an identification of that derivative with a raw ordinary
boundary derivative; the ordinary adapters remain those of the
full source.

## 2. All second-period node values and adjacent ratios are nonzero

The accepted physical Casoratian formula is
\[
\begin{split}
 \mathbf H_{bc}\mathbf Z_{b+1,c}
      -\mathbf H_{b+1,c}\mathbf Z_{bc}
 &=\mathcal W_{bc}\\
 &=\frac rN\,
   \frac{\exp\{\pi i[b-(b^2+3b)/N]\}}
      {(1-r^{b+1})^2P_bP_c}\in K_N\setminus\{0\},
\end{split}
 \tag{13}
\]
for \(0\le b\le N-2,\ 0\le c<N\).
Substitution of (10) cancels its \(\theta_N\) terms:
\[
        \mathbf H_{bc}\mathbf R_{b+1,c}
           -\mathbf H_{b+1,c}\mathbf R_{bc}
                                      =\mathcal W_{bc}\ne0.
 \tag{14}
\]
The only number-theoretic input below is the classical
transcendence of \(\pi\). It implies that \(\theta_N\) is
transcendental over the algebraic numbers.

**Theorem 2.** For every \(N\ge3\),
\[
                  \mathbf Z_{bc}\ne0\qquad(0\le b,c<N).
 \tag{15}
\]
Moreover every adjacent incoming ratio
\[
            \rho_{bc}=\frac{\mathbf Z_{b+1,c}}{\mathbf Z_{bc}},
                  \qquad 0\le b\le N-2,\quad0\le c<N,
 \tag{16}
\]
is transcendental over the algebraic numbers.

*Proof.* If \(\mathbf Z_{bc}=0\), (10) and transcendence imply
\(\mathbf H_{bc}=\mathbf R_{bc}=0\).
This contradicts (14), using the pair starting at \(b\) when
\(b<N-1\), and the pair starting at \(N-2\) when \(b=N-1\).
Thus all denominators in (16) are nonzero.

If \(\rho_{bc}\) were algebraic, then
\[
 \theta_N(\mathbf H_{b+1,c}-\rho_{bc}\mathbf H_{bc})
       +(\mathbf R_{b+1,c}-\rho_{bc}\mathbf R_{bc})=0
 \]
would force both algebraic coefficients to vanish. This contradicts
their determinant (14). \(\square\)

Consequently no nonzero algebraic row \((u,v)\) can annihilate
the physical neighboring second-period state:
\[
                  u\mathbf Z_{bc}+v\mathbf Z_{b+1,c}\ne0.
 \tag{17}
\]
The assertion is specific to these two entries and is exact, not
quantitative in \(N\). It says nothing about a longer observation
row, or about the same row applied to \(\mathbf H\).

The original finite compiler has algebraic entries at physical
ordinary boundary colors: its crossing matrices, turn, multiplication
tensor, trace, and ordinary normal derivatives are all in \(K_N\).
This follows from their displayed formulas in
[arbitrary-power compilation](research_arbitrary_power_source_compilation.md).
Hence the calibrated row \((-\rho_{bc},1)\) cannot literally be
a nonzero original algebraic two-node closing row, even up to an
overall scalar. This statement concerns the ordinary finite
coordinates. It does not identify an arbitrary parameter derivative
with an ordinary normal, or prohibit a different, longer original
observation from having the desired action.

## 3. Subtracting the transcendental constant changes the observed contribution

On the original common analytic parameter domain define the exact
homogeneous companion
\[
       \mathscr R_N(a,y)=Z_N(a,y)-\theta_NH_N(a,y).
 \tag{18}
\]
It satisfies the same homogeneous incoming equation and mixed
contiguity equations, since \(\theta_N\) is constant in the
parameters. Its full physical matrix is exactly \(\mathbf R\).
Its Casoratian with \(H_N\) is unchanged by the subtraction.

This does not preserve the exponentially flat second period.
To see the added component without assuming a packet for \(H_N\),
retain the exact calibrated observation from
[the complementary-observation theorem](research_mixed_three_fourier_calibrated_homogeneous_observation.md):
\[
 \mathcal D_N f
       =f(a+1/N,y)-\frac{Z_N(a+1/N,y)}{Z_N(a,y)}f(a,y).
 \tag{19}
\]
On its actual type-three parameter neighborhood, for large \(N\),
it obeys \(\mathcal D_NZ_N=0\) and
\[
       \mathcal D_NH_N
          =N^{-1/2}\mathcal C_O e^{N\Phi_1}(1+O(N^{-1})),
                         \qquad \mathcal C_O\ne0 .
 \tag{20}
\]
Therefore
\[
 \boxed{\quad
 \mathcal D_N\mathscr R_N
      =-\frac{\mathcal C_O}{2\pi i}\,
                N^{-5/2}e^{N\Phi_1}(1+O(N^{-1})).
 \quad}
 \tag{21}
\]
All scalars and the original left action are unchanged. Thus the
algebraic companion has a proved nonzero left-action observed
component; the old flat-period bound cannot simply be assigned to
it. Equation (21) is still the specified observation (19), not an
arbitrary knot closing functional.

## 4. The precise adjacent-component coefficient

Keep the original matrices of full-node composition:
\[
 \mathsf P=\operatorname{diag}(P_b),\quad
 \mathsf D=\operatorname{diag}((-q)^{-b}),\quad
 S=\operatorname{diag}\left(
       \frac{\kappa^{-1}(-q)^{-b}}{P_b}\right)M,\quad
 \mathsf B=\kappa\mathsf D M^{-1}\mathsf D^{-1}.
 \tag{22}
\]
They all have entries in \(K_N\). The actual two-block identity is
\[
             A_2^2=S^{-1}\mathsf P^{-1}
                        \mathbf H\mathsf B\mathbf H\mathsf D.
 \tag{23}
\]
In particular the intervening matrix is still the actual crossing
interface; it is not replaced by a conjugate pairing.

For every row \(\lambda^T\) with algebraic entries and every fixed
physical output \(c\), (10) gives the stronger exact consequence
\[
 \boxed{\quad
 \lambda^T\mathsf B\mathbf Z_{\cdot c}=0
 \quad\Longleftrightarrow\quad
 \lambda^T\mathsf B\mathbf H_{\cdot c}
       =\lambda^T\mathsf B\mathbf R_{\cdot c}=0 .
 \quad}
 \tag{23a}
\]
Indeed the left side is
\(\theta_N\lambda^T\mathsf B\mathbf H_{\cdot c}
 +\lambda^T\mathsf B\mathbf R_{\cdot c}\), whose two coefficients
are algebraic. Transcendence proves the equivalence.
Thus an original algebraic closing row cannot exactly annihilate
the second period while retaining the homogeneous contribution
at that physical output. This is not a vanishing statement for
the prescribed row applied to the full homogeneous source.

Introduce a formal variable \(t\), with
\(\mathbf Z(t)=t\mathbf H+\mathbf R\).
For any original incoming row \(\ell^T\) and final column \(b\)
with entries in \(K_N\), the polynomial
\[
 Q_{\ell,b}(t)=
   \ell^TS^{-1}\mathsf P^{-1}
         \mathbf Z(t)\mathsf B\mathbf Z(t)\mathsf D b
                        \in K_N[t]
 \tag{24}
\]
has degree at most two and satisfies the exact identities
\[
 \boxed{\quad
 [t^2]Q_{\ell,b}(t)=\ell^TA_2^2b,\qquad
 Q_{\ell,b}(\theta_N)=
   \ell^TS^{-1}\mathsf P^{-1}
                \mathbf Z\mathsf B\mathbf Z\mathsf D b .
 \quad}
 \tag{25}
\]
For \(k\) adjacent power-two components, the analogous degree-\(k\)
coefficient of
\[
 \ell^TS^{-1}\mathsf P^{-1}\mathbf Z(t)
                [\mathsf B\mathbf Z(t)]^{k-1}\mathsf D b
 \tag{26}
\]
is the original \(\ell^TA_2^k b\).
For a fixed branched finite source, one can instead use one formal
variable for each substituted block; its coefficient of their
product is the original source. This follows from the original
multilinear contraction, keeping its multiplication tensor and all
ordinary normal adapters. It does not replace branching by a
coordinatewise node product.

Transcendence makes evaluation of these \(K_N\)-polynomials at
\(\theta_N\) injective. This is only an algebraic uniqueness
statement. In particular, a nonzero value of (24) at \(\theta_N\)
does not imply that its top coefficient in (25) is nonzero.
The vertical packet for each second period likewise supplies no
bound for extraction of that coefficient after the actual signed
interface.

Equations (10), (14), and (25) identify the remaining issue
concretely. The calibrated second-period annihilator is not the
original algebraic two-node closure, and replacing it by an
algebraic homogeneous companion adds a left-action component.
The prescribed adjacent scalar is a particular coefficient of
the complete period contraction. Its noncancellation and its
geometric asymptotic remain to be proved.
