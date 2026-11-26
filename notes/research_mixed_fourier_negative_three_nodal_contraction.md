# Exact nodal contraction of the three-negative-crossing source

Research deduction, 7 November 2026. The pole values of the complete
three-negative-crossing cap may replace that cap in its original
physical-node contraction exactly. Both four-type sectors and every
normal already present in the compiled source are retained.
For more general observations the same values determine the complete
cardinal interpolant, and the original observation acts on that
interpolant, not on the raw pole function.

For a positive three/four path ending in four, this operation changes
the last vertex to power one. Its marked elimination is the already
proved degree-two unit move, not a new arbitrary short-filling theorem.
The note makes the exact source and normal bookkeeping explicit.
No numerical evaluation is used.

## 1. The finite values determine the entire incoming band

Use \(D=N-1\), \(q=e^{\pi i/N}\), \(r=q^{-2}\), \(P_b=(r;r)_b\),
\(\kappa=e^{\pi iD^2/(2N)}\), \(X=e^{-2\pi ia}\) and
\(Y=e^{2\pi iy}\). Let \(G_{-3,N}=\mathcal M_{-3}Z_N\) be the
whole original source. The
[complete source identity](research_mixed_fourier_negative_three_full_source.md),
Proposition 2, proves at every incoming node
\[
 G_{-3,N}(r^b,y)=\pi_{b,N}(y),\qquad
 \pi_{b,N}(y)=
 \frac{\kappa^{-3}e^{\pi iDy}}N
                \frac{(r/Y)^b(Y;r)_b}{P_b},
 \qquad 0\le b<N .
 \tag{1}
\]
Here and below \(G_{-3,N}(X,y)\) denotes the same negative-band
function with its first argument written exponentially. Formula
(1) is a finite product identity for all complex \(y\), including
all of its numerator zeros. Its factorial denominators are nonzero.
It does not rely on a regular large-\(N\) pole chart at the endpoint
indices.

Define
\[
 L_{b,N}(X)=\frac1N\sum_{j=0}^{D}(r^b/X)^j,\qquad
 L_{b,N}(r^c)=\delta_{bc}.
 \tag{2}
\]
The same source has incoming Laurent band \([-D,0]\). Consequently
\[
 \boxed{\quad
 G_{-3,N}(X,y)=\sum_{b=0}^{D}L_{b,N}(X)\pi_{b,N}(y).
 \quad}
 \tag{3}
\]
Indeed both sides have that band and the same \(N\) distinct values.
This proves equality of the entire finite functions, not only their
values. All parameter derivatives of (3) are therefore exact.

In a regular pole chart the
[pole/current decomposition](research_mixed_fourier_negative_three_pole_current.md)
is \(G_{-3,N}=\mathcal P_{-3,N}+\mathcal J_{-3,N}\).
The current vanishes at the physical nodes, so (3) is precisely the
negative-band cardinal interpolation of the pole values. It is
generally not the raw function \(\mathcal P_{-3,N}(a,y)\).

## 2. The literal prefix pairing needs only those values

Let \(F_N\) be any polynomial of degree less than \(N\), with
coefficients allowed to depend on other retained variables, and
let \(\eta\in\{0,1\}\). Put
\[
 W_{\eta,N}(X)=\{d_N(X)(1+X^{-N})\}^{\eta}.
 \tag{4}
\]
The original [literal pairing](research_mixed_literal_transfer_norm_obstruction.md),
equation (7), and (1) give
\[
 \boxed{\begin{split}
 &N\operatorname{CT}_X
       [F_N(X)W_{\eta,N}(X)G_{-3,N}(X,y)]\\
 &\qquad=
 \frac{\kappa^{-3}e^{\pi iDy}}N
      \sum_{b=0}^{D}
       F_N(r^b)\frac{(r/Y)^b(Y;r)_b}{P_b^{\,1+\eta}} .
 \end{split}}
 \tag{5}
\]
This is an exact signed sum. When \(\eta=1\), the left side retains
the sum of its two distinct constant-term sectors. It is their sum,
not either sector separately, that equals the physical-node pairing.
The equality \(X^{-N}=1\) at the nodes does not identify those
sectors individually.

For completeness, the band of \(F_NG_{-3,N}\) is contained in
\([-D,D]\). With \(\eta=0\), node averaging extracts only its
constant coefficient. With \(\eta=1\), multiply by the degree-\(D\)
polynomial \(d_N\): the band becomes \([-D,2D]\), so averaging
extracts exactly its coefficients of degrees zero and \(N\).
These are the coefficients selected by \(1+X^{-N}\), and
\(d_N(r^b)=P_b^{-1}\). This proves (5), including both parities.

Thus no off-grid signed current remains to be estimated at this
particular contraction. It has been included exactly through the
finite-band source before node averaging. Formula (5) supplies no
sign or nonzero leading coefficient for the remaining sum.

## 3. The actual last-power-one path source and its scalar

Start with a word of length \(m\ge2\), flags
\(\epsilon_1,\ldots,\epsilon_m\in\{0,1\}\), \(\epsilon_m=1\),
and put \(k=\sum_j\epsilon_j\), \(\eta=\epsilon_{m-1}\).
Use the literal prefix recursion from
[the exact message bridge](research_mixed_conditional_fourier_message_bridge.md):
\[
 F_1=U_{\epsilon_1,N}(w,\cdot),\qquad
 F_{j+1}=\mathcal T_{\epsilon_j\epsilon_{j+1}}F_j
                         \quad(1\le j<m-1).
 \tag{6}
\]
Each \(F_j\) has degree less than \(N\) in its retained variable.
Every physical support and normal is already part of that exact
recursion.

The original Fourier-ended source and its contracted right cap obey
\[
 v(w)^TA_{3+\epsilon_1}\cdots A_4h(y)
   =\kappa^{m+k}N^k\,
       N\operatorname{CT}_X
                  [F_{m-1}(X)W_{\eta,N}(X)Z_N(X,y)] .
 \tag{7}
\]
This is equations (6)--(9) of the message bridge, or equivalently
the scalar in
[Fourier-ended boundary windows](research_mixed_fourier_ended_boundary_windows.md),
equation (6), after performing the earlier prefix contractions.

Apply \(\mathcal M_{-3}\) only to the output \(y\). It commutes with
the finite prefix contractions, and
\(A_4M^{-3}=JM=A_1\). Hence (5) proves
\[
 \boxed{\begin{split}
 &v(w)^TA_{3+\epsilon_1}\cdots
                         A_{3+\epsilon_{m-1}}A_1h(y)\\
 &\qquad=
 \kappa^{m+k-3}N^{k-1}e^{\pi iDy}
       \sum_{b=0}^{D}
       F_{m-1}(r^b)
                 \frac{(r/Y)^b(Y;r)_b}{P_b^{\,1+\eta}} .
 \end{split}}
 \tag{8}
\]
All ordinary or Fourier derivatives of (8) are exact. In particular
there is no inference from a small off-grid remainder, nor a division
by a zero incoming weight.

The physical turn in \(A_1=JM\) has not been deleted. The old
[degree-two source reduction](research_degree_two_short_reductions.md),
Proposition 1, already proves in the full original algebra
\[
            \mathcal J_1
                =\kappa(R^{-1}\otimes R^{-1})\mathcal K .
 \tag{9}
\]
Its [marked tangle version](research_marked_degree_two_tangle_moves.md)
keeps the actual rotations, crossing disks, framings and two
neighboring inverse twists. Thus (8) is an exact Fourier
representative of an available unit-vertex reduction. It does not
prove estimates for the shifted/rotated neighboring source, nor
permit (9) at a higher-valence vertex.

## 4. Normals and arbitrary literal contexts

Let \(\mathscr L_N\) be any original linear observation of the
incoming band, after all its other inputs have been fixed. Equation
(3) gives exactly
\[
       \mathscr L_NG_{-3,N}
            =\sum_{b=0}^{D}
                   \mathscr L_N(L_{b,N})\,\pi_{b,N}(y).
 \tag{10}
\]
This includes parameter differentiation of the finite interpolant.
It also includes the original ordinary Hermite observations after
their specified full coordinate adapter. For example (3) of the
all-power source note gives the explicit original-coordinate form
\[
   \ell_N^TM^*h(y)
       =\kappa^2N\sum_{b=0}^{D}
                         (\ell_N)_b(-q)^b\pi_{b,N}(y)
 \tag{11}
\]
for any original coefficient row \(\ell_N^T\).
Indeed at \(a=b/N\),
\(G_{-3,N}=(-q)^{-b}(M^*h)_b/(\kappa^2N)\).
All coefficients of a context built from turns, fixed crossings,
multiplication and the final trace may be retained in \(\ell_N\),
as in the
[original source compiler](research_arbitrary_power_source_compilation.md).
At a branch, multilinearity applies (10) in each occupied input
slot, keeping its full original tensor.

None of this equates pole derivatives with source derivatives.
The [complete connection formula](research_mixed_fourier_negative_three_connection.md),
equation (14a), gives at interior physical nodes
\[
 \partial_a(G_{-3,N}-\mathcal P_{-3,N})(b/N,y)
   =2\pi i\,\kappa^{-3}N^{-2}e^{\pi iDy}
                       (1-Y^{-N})V_N(b/N,y),
 \tag{12}
\]
whose leading coefficient is nonzero on the stated compact domains.
One must differentiate the cardinal interpolation in (3), or use
the original adapter in (10)--(11); differentiating the raw pole
would omit (12).

There is also a simple algebraic reason not to replace a branching
tensor by pointwise multiplication of Fourier-node values.
The full ordinary algebra
\[
                    \mathcal A_N=\mathbb C[z]/(2T_N(z/2)+2)
 \tag{13}
\]
has a nonzero square-zero element for every \(N\ge2\).
For instance the product of its distinct linear root factors is
nonzero in (13), has degree less than \(N\), and its square is
divisible by the defining polynomial. Some roots are double at
every such level. By contrast, \(\mathbb C^N\) with coordinatewise
multiplication has no nonzero nilpotents. An invertible linear
adapter to its node values therefore cannot be multiplicative:
otherwise that square-zero element would map to zero, contradicting
injectivity.

Accordingly the pole values may replace the complete short source
in every literal context **with the context's original linear or
multilinear adapter retained**. There is no loss of normal data in
that operation. What is not justified is a bare pole substitution
inside a differential observation, a pointwise branching rule, or
an asymptotic lower bound for the new finite sum. The unit reduction
does not close arbitrary short partial fillings, but it isolates the
remaining problem in the actual transformed neighboring source
instead of an unneeded off-grid current estimate at a simple-node
interface.
